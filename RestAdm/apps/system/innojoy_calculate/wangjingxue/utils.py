# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = xiongliff
__mtime__ = '2019/9/23'
"""
import numpy as np
def get_end_year(file_name):
    """
    通过file_name获取截止时间，先根据_切割，再根据.切割
    :param file_name:
    :return:
    """
    end_year_str = file_name.split('_')[1].split('.')[0]
    return int(end_year_str)


def split_sub_class_string(sub_class_str):
    """
    切割子分类号string
    :param sub_class_str:
    :return:
    """
    init_sub_class_list = sub_class_str.split(';')
    res_list = list()
    if init_sub_class_list:
        for init_sub_class in init_sub_class_list:
            res_list.append(init_sub_class.split('.')[0])
    return res_list

def save_data_list(save_path, save_list):
    """
    将文件以txt格式保存
    :param save_array:
    :return:
    """
    with open(save_path, 'w+') as f:
        for row_data in save_list:
            for col_data in row_data:
                f.write(str(col_data))
                f.write(" ")
            f.write("\n")
    f.close()