# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = xiongliff
__mtime__ = '2019/9/3'
"""

import system.innojoy_calculate.utils.read_mat_data as read_mat
import system.innojoy_calculate.utils.split_time_window as st
import system.innojoy_calculate.wangjingxue.calculate_mat_data as cm
import pandas as pd
import numpy as np
if __name__ =="__main__":
    
    data_array = np.load('d:\\2005_2009.npy', allow_pickle=True)
    data_name_str = 'd:\\2005_2009.npy'
    params_list = cm.get_inventor_params(data_array, data_name_str)
    inventor_patents_count_dict = params_list[0]
    inventor_patents_label_dict = params_list[1]
    inventor_pantents_bwt_dict = params_list[2]
    inventor_patents_rows_dict = params_list[3]
    #res = cm.calculate_inv_perf(data_array, data_name_str)
    key_inventor_list = cm.get_key_inventor(data_array, data_name_str)
    res = list()
    for key_inventor in key_inventor_list:

        aa = cm.calculate_key_inventor_hole_label(data_array,inventor_patents_rows_dict,key_inventor)
        res.append(aa)
    print(res)
    data = read_mat.read_base_data('D:/test.mat',True)
    ss = st.get_start_end_year(data)
    kwargs_dict = dict()
    kwargs_dict['time_start'] = ss[0]
    kwargs_dict['time_end'] = ss[1]
    kwargs_dict['window_length'] = 5
    st.split_overlapping_windows(data,kwargs_dict)
    # data = list()
    # data.append(['1991/1/1','1'])
    # data.append(['1992/1/1','2'])
    # array = np.array(data)[:,0]
    # print min(array)
    # a= list()
    # a.append([1,2,3])
    # a.append([2,3,4])
    # b =np.array(a)
    # print a
    # print b
    #


