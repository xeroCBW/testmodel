# -*- coding: utf-8 -*-
"""
__title__ = '按照不同的方式切割分类号'
__author__ = xiongliff
__mtime__ = '2019/6/19'
"""
import exceptions


def split_by_type(class_nbr_string, calculate_type):
    """
    根据type按照不同的方式切割分类号
    :param class_nbr_string
    :param caculate_type:
    :return:
    """
    if calculate_type == 1:
        # 第一种方式按照截取前4个字符
        return class_nbr_string[0:4]
    elif calculate_type ==2:
        # 第二种统计方式，截取/号前的字符
        return class_nbr_string.split("/")[0]
    elif calculate_type ==3:
        # 第三种统计方式，截取小括号前的字符
        return class_nbr_string.split("(")[0]
    elif calculate_type ==4:
        #第4种统计方式，截取前3个字符
        return class_nbr_string[0:3]
    else:
        raise exceptions('输入的计算方式有误')