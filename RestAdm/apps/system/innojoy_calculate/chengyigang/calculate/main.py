# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = xiongliff
__mtime__ = '2019/7/20'
"""

from chengyigang.calculate import calculate

from utils import read_xls_data



if __name__ == '__main__':
    base_data_list = read_xls_data.read_data()
    result_dict = dict()
    for i in range(20):
        threshold = 0.1 * i
        result_dict[threshold] = calculate.calculate_rate(base_data_list,threshold,1)
    print(str(result_dict))