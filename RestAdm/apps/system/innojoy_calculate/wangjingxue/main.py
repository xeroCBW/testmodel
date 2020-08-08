# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = xiongliff
__mtime__ = '2019/9/25'
"""

import utils.read_mat_data as read_mat
import utils.split_time_window as st
import wangjingxue.calculate_mat_data as cm
import wangjingxue.utils as ut
import numpy as np
import datetime


def calculate_over_lapp_window(file_path, window_length, except_window_length = 3, save_path = 'd:/',
                               has_header = True):
    """
     计算重叠时间窗口下的数据
    :param file_path:mat文件的地址
    :param window_lenth:时间窗口的长度
    :param except_window_lenth: 用于计算联系人知识宽度。深度，排除在时间窗口（3年）内合作过的研发者
    :param save_path:保存文件地址
    :param has_header:
    :return:
    """
    # 获取原始数据
    base_data_all = read_mat.read_base_data(file_path, has_header)
    # 根据原始数据，按照时间窗口长度，切割，并保存为不同的文件
    time_start = st.get_start_end_year(base_data_all)[0]
    time_end = st.get_start_end_year(base_data_all)[1]
    kwargs_dict = dict()
    kwargs_dict['time_start'] = time_start
    kwargs_dict['time_end'] = time_end
    kwargs_dict['window_length'] = window_length
    #保存文件
    save_name_list = st.split_overlapping_windows(base_data_all, kwargs_dict)
    # 计算所有数据中研发者第一次申请专利的时间
    inventor_first_year_dict = cm.get_first_patent_year(base_data_all)
    # 循环计算不同的时间窗口内的关键研发者指标，先按时间窗口循环,再计算其中关键研发者指标
    
    res = calculate_all_target(save_name_list, except_window_length, inventor_first_year_dict)
    #保存
    save_res_path = save_path + 'overlapp_window.txt'
    #结果有14列
    ut.save_data_list(save_res_path , res)


def calculate_not_over_lapp_window(file_path, window_length, except_window_length=3, save_path='d:/', has_header=True):
    """
     计算不重叠时间窗口下的数据
    :param file_path:
    :param window_lenth:
    :param except_window_lenth: 用于计算联系人知识宽度。深度，排除在时间窗口（3年）内合作过的研发者
    :param save_path:
    :param has_header:
    :return:
    """
    # 获取原始数据
    base_data_all = read_mat.read_base_data(file_path, has_header)
    # 根据原始数据，按照时间窗口长度，切割，并保存为不同的文件
    time_start = st.get_start_end_year(base_data_all)[0]
    time_end = st.get_start_end_year(base_data_all)[1]
    kwargs_dict = dict()
    kwargs_dict['time_start'] = time_start
    kwargs_dict['time_end'] = time_end
    kwargs_dict['window_length'] = window_length
    # 保存文件
    save_name_list = st.split_not_overlapping_windows(base_data_all, kwargs_dict)
    # 计算所有数据中研发者第一次申请专利的时间
    inventor_first_year_dict = cm.get_first_patent_year(base_data_all)
    # 循环计算不同的时间窗口内的关键研发者指标，先按时间窗口循环,再计算其中关键研发者指标
    
    res = calculate_all_target(save_name_list, except_window_length, inventor_first_year_dict)
    # 保存
    save_res_path = save_path + 'not_overlapp_window.txt'
    # 结果有14列
    ut.save_data_list(save_res_path, res)
    
    
    
def calculate_all_target(save_name_list, except_window_length, inventor_first_year_dict):
    """
    
    :param base_data_all:
    :param save_path:
    :param save_name_list:
    :param except_window_length:
    :param inventor_first_year_dict:
    :return:
    """
    res_list = list()
    for save_name in save_name_list:
        one_window_res = calculate_target_one_window(save_name, except_window_length,inventor_first_year_dict)
        res_list.extend(one_window_res)
    return res_list

def calculate_target_one_window(save_name, except_window_length, inventor_first_year_dict):
    one_window_res = list()
    time_start = save_name.split('_')[0][:-4]
    time_end = save_name.split('_')[1].split('.')[0]
    split_file_name = save_name
    data_array = np.load(split_file_name, allow_pickle=True)
    params_list = cm.get_inventor_params(data_array, split_file_name)
    inventor_patents_count_dict = params_list[0]
    inventor_patents_label_dict = params_list[1]
    inventor_patents_bwt_dict = params_list[2]
    inventor_patents_rows_dict = params_list[3]
    key_inventor_list = cm.get_key_inventor(data_array, split_file_name)
    inv_perf_dict = cm.calculate_inv_perf(inventor_patents_count_dict, inventor_patents_label_dict,
                                          inventor_patents_bwt_dict)
    for key_inventor in key_inventor_list:
        key_inventor_res = list()
        # 加入id
        key_inventor_res.append(key_inventor)
        # 加入窗口的起始时间
        key_inventor_res.append(time_start)
        # 加入创造力
        key_inventor_res.append(inv_perf_dict[key_inventor])
        [structural_hole, key_inventor_degree] = cm.calculate_key_inventor_hole_label(data_array,
                                                                                      inventor_patents_rows_dict,
                                                                                      key_inventor)
        # 加入结构洞指数
        key_inventor_res.append(structural_hole)
        
        [knowledge_depth, knowledge_breath] = cm.calculate_depth_breath_knowledge(data_array,
                                                                                  inventor_patents_rows_dict,
                                                                                  key_inventor)
        # 加入关键研发者知识深度
        key_inventor_res.append(knowledge_depth)
        # 加入关键研发者知识宽度
        key_inventor_res.append(knowledge_breath)
        # 计算联系人数量，知识深度，宽度
        [contacts_size, contacts_knowledge_depth,
         contacts_knowledge_breath] = cm.calculate_contacts_depth_breath_knowledge(data_array, save_name,
                                                                                   inventor_patents_rows_dict,
                                                                                   key_inventor, except_window_length)
        # 加入联系人知识深度
        key_inventor_res.append(contacts_knowledge_depth)
        # 加入联系人知识宽度
        key_inventor_res.append(contacts_knowledge_breath)
        # 加入中心度
        key_inventor_res.append(key_inventor_degree)
        # 加入平均关系强度
        tie_strength = cm.calculate_key_inventor_tie_strength(data_array, inventor_patents_rows_dict, key_inventor)
        key_inventor_res.append(tie_strength)
        
        # 加入职业年龄
        
        career_age = cm.get_key_inventor_career_age(data_array, inventor_patents_rows_dict, key_inventor,
                                                    inventor_first_year_dict)
        key_inventor_res.append(career_age)
        # 计算个人能力,观测年采用的是时间窗口的截止时间
        individual_quality = inventor_patents_count_dict[key_inventor]
        key_inventor_res.append(individual_quality)
        # 计算流动性
        mobility = cm.calculate_mobility(data_array, inventor_patents_rows_dict, key_inventor)
        key_inventor_res.append(mobility)
        # 联系人数量
        key_inventor_res.append(contacts_size)
        one_window_res.append(key_inventor_res)
    return one_window_res

if __name__ == '__main__':
    """
    使用说明：
    1.分为2个函数，一种是折叠时间窗口的calculate_over_lapp_window，一种是不折叠时间窗口下的，calculate_over_lapp_window。
    2.设计的思路：
        因为文件比较大，且是mat格式文件，读入python较慢，因此考虑根据时间窗口将文件切割保存，这样缩小计算范围，加快
      计算速度，同时可以将两种时间窗口的计算抽象出来。
    3.使用方式:
        a.根据需求修改参数：mat文件位置，时间窗口大小，在区分联系人时的时间窗口大小，保存文件位置，原文件中是否有标题头
        b.然后调用对应的函数
        c.直接运行该文件，
        例子如下：
        结果保存在文件位置 + not_overlapp_window.txt or overlapp_window.txt
        结果集的列对应的含义如下：
            id
            窗口的起始时间
            创造力
            结构洞指数
            关键研发者知识深度
            关键研发者知识宽度
            联系人知识深度
            联系人知识宽度
            中心度
            平均关系强度
            职业年龄
            个人能力
            流动性
            联系人数量
    4.问题：a.在测试数据中发现有1条1915年的数据，导致时间窗口切割过多，由于不知是否为无效数据，所以未做删除或过滤
        由于这个原因，程序在运行结果中，有的时间窗口中的数据为空 =》有的时间窗口下无数据计算结果，并可能有warning
        警告，不影响其他结果
        
    """
    calculate_not_over_lapp_window('D:/test.mat',10,except_window_length = 3, save_path = 'd:/',
                               has_header = True)
    calculate_over_lapp_window('D:/test.mat',10)