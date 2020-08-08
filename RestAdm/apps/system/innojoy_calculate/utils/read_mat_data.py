# -*- coding: utf-8 -*-
"""
__title__ = '读取mat文件的工具类'
__author__ = xiongliff
__mtime__ = '2019/9/3'
"""

import scipy.io as sio
import numpy as np
import datetime
from innojoy_calculate.wangjingxue import  const
def read_base_data(file_path, has_header, data_name = 'DataAll1'):
    """
    使用scipy包来读取mat文件
    :param file_path:mat文件的地址
    :param data_name:需要读取的workspacename
    :param has_header:是否带列头
    :return: list
    """
    read_data_dict = sio.loadmat(file_path)
    data_array = read_data_dict[data_name]
    result_list = list()
    if has_header:
        data_list = data_array[1:].tolist()
        
    else:
        data_list = data_array.tolist()
    #转换
    for row_data in data_list:
        element_data = list()
        for index ,col_data in enumerate(row_data):
            #因为原始数据中有2维数组数据不方便后面提取与计算，因此先统一处理一下
            #转为一维数据，存到list中，并且对其中的nan数据进行处理
            # 判断是否为nan
            element = col_data.flatten()
            if index == const.INVENTOR_COL:
                if np.isnan(element).any():
                    element_data.append(None)
                else:
                    element_data.append(','.join([str(item)for item in element]))
            else:
                if element.size == 0 or not element[0] == element[0]:
                    element_data.append(None)
                
                else:
                    element_data.append(element[0])
                
                
        result_list.append(element_data)
    return result_list
    

def read_split_time_data(file_path):
    return np.load(file_path, allow_pickle=True)


if __name__ == '__main__':
    t1 = datetime.datetime.now()
    a = read_base_data('D:/test.mat',True)
    
    t2 = datetime.datetime.now()
    print(t2-t1)
    