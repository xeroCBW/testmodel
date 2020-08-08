# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = xiongliff
__mtime__ = '2019/7/20'
"""

from utils import read_xls_data

from chengyigang.draw_curve import draw_class_nbr_rate

if __name__ == '__main__':
    base_data_list = read_xls_data.read_data()
    draw_class_nbr_rate.draw_class_number_curve(base_data_list)