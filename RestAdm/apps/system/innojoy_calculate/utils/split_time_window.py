# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = xiongliff
__mtime__ = '2019/8/19'
"""
import numpy as np
import scipy.io as sio
from wangjingxue import const
def split_overlapping_windows(base_data, kwargs_dict, save_path = 'd:/'):
    """
    根据时间窗口来切割并保存数据，这是重叠的时间窗口，
    切割结果如window_length=3,则按3年时间窗口切割，1990-1992,1991-1993,1992-1994，
    保存的数据格式如：base_data_overlapping#1990#1992
    :param base_data:原始数据
    :param time_start:起始时间
    :param time_end:终止时间
    :param window_length时间窗口的长度
    :return:
    """
    #计算有多少个时间窗口
    #起始时间大于终止时间直接返回
    time_start = kwargs_dict['time_start']
    time_end = kwargs_dict['time_end']
    window_length = kwargs_dict['window_length']
    # 时间窗口的数量=（终止时间 -窗口长度）+1 -起始时间 +1
    window_count = time_end - window_length - time_start + 2
    save_name_list = list()
    if window_count < 0 :
        #只有一个时间窗口
        year_end = int(time_start) + window_length - 1
        save_name =  save_path + time_start + '_' + str(year_end)+'.npy'
        save_data = np.array(base_data)
        np.save(save_name, save_data)
        save_name_list.append(save_name)
    else:
        window_start = time_start
        #创建一个保存各个时间窗口数据的dict
        split_data_dict = {str(time_start + window_num): list() for window_num in range(window_count)}
       
        #循环读取base_data数据并将其保存到各自对应的时间窗口
        for row_data in base_data:
            #截取年份
            application_date_year = row_data[const.APP_YEAR_COL]
            save_row_into_dict(split_data_dict, application_date_year, row_data, kwargs_dict)
           
        #保存
        
        for year_key in split_data_dict:
            year_end = int(year_key) + window_length - 1
            save_name = save_path + year_key + '_' + str(year_end)+'.npy'
            #save_data = split_data_dict[year_key]
            save_name_list.append(save_name)
            save_data = np.array(split_data_dict[year_key])
            np.save(save_name,save_data)
    return save_name_list


def split_not_overlapping_windows(base_data, kwargs_dict, save_path='d:/'):
    """
    根据时间窗口来切割并保存数据，这是不重叠的时间窗口，
    切割结果如window_length=3,则按3年时间窗口切割，1990-1992,1993-1995,1996-1998，
    保存的数据格式如：
    :param base_data:原始数据
    :param time_start:起始时间
    :param time_end:终止时间
    :param window_length时间窗口的长度
    :return:
    """
    # 计算有多少个时间窗口
    # 起始时间大于终止时间直接返回
    time_start = kwargs_dict['time_start']
    time_end = kwargs_dict['time_end']
    window_length = kwargs_dict['window_length']
    # 时间窗口的数量
    window_count = (time_end - time_start + 1) // window_length
    save_name_list = list()
    if window_count < 0:
        # 只有一个时间窗口
        year_end = int(time_start) + window_length - 1
        save_name = save_path + time_start + '_' + str(year_end) + '.npy'
        save_data = np.array(base_data)
        np.save(save_name, save_data)
        save_name_list.append(save_name)
    else:
        window_start = time_start
        # 创建一个保存各个时间窗口数据的dict
        split_data_dict = {str(time_start + window_num * window_length): list() for window_num in range(window_count)}

        # 循环读取base_data数据并将其保存到各自对应的时间窗口
        for row_data in base_data:
            # 截取年份
            application_date_year = row_data[const.APP_YEAR_COL]
            save_row_into_dict2(split_data_dict, application_date_year, row_data, kwargs_dict)

        # 保存
        
        for year_key in split_data_dict:
            year_end = int(year_key) + window_length - 1
            save_name = save_path + year_key + '_' + str(year_end) + '.npy'
            # save_data = split_data_dict[year_key]
            save_name_list.append(save_name)
            save_data = np.array(split_data_dict[year_key])
            np.save(save_name, save_data)
    return save_name_list


def get_start_end_year(base_data):
    """
    获取base_data中起始和终止时间
    :param base_data:
    :return: [start_year, end_year]
    """
    #取出第26列为application_date列
    application_date_array = np.array(base_data)[:, const.APP_YEAR_COL]
    application_date_start = min(application_date_array)
    application_date_end = max(application_date_array)
    return [application_date_start, application_date_end]



def extract_year_from_str(date_str):
    """
    从'1992/12/01'字符串中取出year
    :param date_str:
    :return:
    """
    # 截取年份
    application_date_year = int(date_str.split('/')[0])
    return application_date_year
    
    
    
def save_row_into_dict(year__data_dict, row_year , row_data ,kwargs_dict):
    """
    有重叠窗口根据row中的application_date将数据保存到各个时间窗口的dict中
    :param year__data_dict:
    :param row_year:
    :param row_data:
    :param kwargs_dict:关于时间窗口以及起始、终止时间参数dict
    :return:
    """
    time_start = kwargs_dict['time_start']
    time_end = kwargs_dict['time_end']
    window_length = kwargs_dict['window_length']
   
    #获取row_year对应的应该保存在哪些时间窗口
    window_key_list = get_year_window_list(time_start, time_end, window_length, row_year)
    for window_key in window_key_list:
        year__data_dict[window_key].append(row_data)


def save_row_into_dict2(year__data_dict, row_year, row_data, kwargs_dict):
    """
    没有重叠窗口根据row中的application_date将数据保存到各个时间窗口的dict中
    :param year__data_dict:
    :param row_year:
    :param row_data:
    :param kwargs_dict:关于时间窗口以及起始、终止时间参数dict
    :return:
    """
    time_start = kwargs_dict['time_start']
    time_end = kwargs_dict['time_end']
    window_length = kwargs_dict['window_length']
    
    window_cnt  = (time_end - time_start + 1) // window_length
    max_window_start = time_start + window_cnt * window_length
    # 获取row_year对应的应该保存在哪些时间窗口
    window_year = get_year_window(time_start, window_length, row_year)
    if window_year < str(max_window_start):
        year__data_dict[window_year].append(row_data)
 
        
        
def get_year_window_list(time_start, time_end, window_length, row_year):
    """
    有重叠窗口，获取row_year对应应该在什么时间窗口
    :param time_start:
    :param time_end:
    :param window_length:
    :param row_year:
    :return:
    """
    #对于一个给定的year,所处的时间窗口：以他为终止的时间窗口-以他为开始的时间
    window_start = row_year - window_length + 1
    window_end = row_year
    max_window_start = time_end - window_length + 1
    if window_start < time_start:
        window_start = time_start
    if row_year > max_window_start:
        window_end = max_window_start
    #时间窗口值为range(window_start, window_end + 1, 1）
    year_window_list = [str(window_year) for window_year in range(window_start, window_end + 1, 1)]
    #去重
    return list(set(year_window_list))


def get_year_window(time_start, window_length, row_year):
    """
    没有重叠窗口，获取row_year对应应该在什么时间窗口
    :param time_start:
    :param time_end:
    :param window_length:
    :param row_year:
    :return:
    """
    #所处的时间窗口
    window_nbr = (row_year - time_start ) // window_length
    window_year = time_start + window_nbr * window_length
    return str(window_year)

if __name__ == '__main__':
    kwargs_dict = dict()
    kwargs_dict['time_start'] = 1990