# -*- coding: utf-8 -*-
"""
__title__ = '统计发明人和申请人的专利个数'
__author__ = xiongliff
__mtime__ = '2019/6/19'
"""
import itertools
from innojoy_calculate.common import const
from innojoy_calculate.utils import split_class_nbr

def count_inventor_patents_by_data(base_data_list):
    """
    统计每个发明人的专利数量
    :param base_data_list:
    :return: 每个发明人的专利数量，如{'张三'：10, '李四'：12}
    """
    inventor_patents_dict = dict()
    for row_data in base_data_list:
        # 读取申请人所在列
        inventor_value = row_data[const.INVENTOR]
        if isinstance(inventor_value, basestring) and inventor_value.strip() != "":
            inventor_value_list = inventor_value.split(";")
            if inventor_value_list:
                for inventor in inventor_value_list:
                    # 判断dict中是否存在该申请人，存在则更新，不存在则插入
                    if inventor not in inventor_patents_dict.keys():
                        inventor_patents_dict[inventor] = 1
                    else:
                        inventor_patents_dict[inventor] += 1
    return inventor_patents_dict


def count_applicant_patents_by_data(base_data_list):
    """
    统计每个申请人的专利数量
    :param base_data_list:
    :return: 每个申请人的专利数量dict，如：{'京东方'：2, '星辰'：4}
    """
    applicant_patents_dict = dict()
    for row_data in base_data_list:
        # 读取发明人所在列
        applicant_value = row_data[const.APPLICANT]
        if isinstance(applicant_value, basestring) and applicant_value.strip() != "":
            applicant_value_list = applicant_value.split(";")
            if applicant_value_list:
                for applicant in applicant_value_list:
                    # 判断dict中是否存在该申请人，存在则更新，不存在则插入
                    if applicant not in applicant_patents_dict.keys():
                        applicant_patents_dict[applicant] = 1
                    else:
                        applicant_patents_dict[applicant] += 1
    return applicant_patents_dict


def count_class_nbr_patent_cnt(base_data_list, calculate_type):
    """
    统计在所有数据中不同分类号对应的专利数量
    :param base_data_list:
    :return:
    """
    class_number_patent_cnt_dict = dict()
    for base_data in base_data_list:
        class_number_value = base_data[const.CLASS_NBR]
        calculate_class_number_patent_count_dict(class_number_value, class_number_patent_cnt_dict, calculate_type)
    return class_number_patent_cnt_dict


def calculate_class_number_patent_count_dict(class_number_value, class_number_dict, calculate_type):
    """
    统计一条记录中分类号中的专利数量，并添加到class_number_dict中
    :param class_number_value:
    :param class_number_dict:
    :param calculate_type:
    :return:
    """
    if isinstance(class_number_value, basestring) and class_number_value.strip() != "":
        class_number_string_list = class_number_value.split(";")
        if class_number_string_list:
            #取出分类号组成新的list
            class_nbr_list = [split_class_nbr.split_by_type(class_nbr_string, calculate_type)
                              for class_nbr_string in class_number_string_list]
            #去重
            class_nbr_list = list(set(class_nbr_list))
            for class_nbr in class_nbr_list:
                # 判断是否有该分类号
                if class_nbr in class_number_dict.keys():
                    class_number_dict[class_nbr] += 1
                else:
                    class_number_dict[class_nbr] = 1
    return class_number_dict

def calculate_unique_class_number_patent_count(class_number_value, class_number_dict, calculate_type):
    """
    统计一条记录中同时有两个分类号的专利数量，并添加到class_number_dict中
    :param class_number_value:
    :param class_number_dict:
    :param calculate_type:
    :return:
    """

    if isinstance(class_number_value, basestring) and class_number_value.strip() != "":
        class_number_string_list = class_number_value.split(";")
        if class_number_string_list:
            #取出分类号组成新的list
            class_nbr_list = [split_class_nbr.split_by_type(class_nbr_string, calculate_type)
                              for class_nbr_string in class_number_string_list]
            #去重
            class_nbr_list = list(set(class_nbr_list))
            if len(class_nbr_list) > 1:
                for class_nbr_array in itertools.combinations(class_nbr_list, 2):
                    #从class_nbr_list中获取所有2个分类号的组合
                    key = class_nbr_array[0] + '#' + class_nbr_array[1]
                    # 判断是否有该分类号
                    if key in class_number_dict.keys():
                        class_number_dict[key] += 1
                    else:
                        class_number_dict[key] = 1
    return class_number_dict

def count_unique_class_nbr_patent_cnt(base_data_list, calculate_type):
    """
    统计同时有两个分类号的专利数量dict
    :param base_data_list:
    :param calculate_type:
    :param unique_class_nbr1:
    :param unique_class_nbr2:
    :return:
    """
    class_number_patent_cnt_dict = dict()
    for base_data in base_data_list:
        class_number_value = base_data[const.CLASS_NBR]
        calculate_unique_class_number_patent_count(class_number_value, class_number_patent_cnt_dict, calculate_type)
    return class_number_patent_cnt_dict