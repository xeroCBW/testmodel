# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = xiongliff
__mtime__ = '2019/7/1'
"""

import difflib
import re
from common import const


def sort_dict_by_value(base_dict):
    """
    根据字典的value进行排序
    :param base_dict:
    :return:
    """
    sort_list = sorted(base_dict.items(), key=lambda x: x[1], reverse=False)
    return {unit[0]: unit[1] for unit in sort_list}


def generate_ignore_character():
    """
    生成删除无效字符的pattern和dict
    :return:
    """
    translate_list = const.USELESS_STRING_LIST
    translate_dict = {items: '' for items in translate_list}
    translate_dict = dict((re.escape(key), value) for key, value in translate_dict.items())
    pattern = re.compile("|".join(translate_dict.keys()))
    return [pattern, translate_dict]


def replace_str(before_string, pattern, translate_dict):
    """
    根据pattern和translate_dict同时替换字符
    :return:
    """
    after_string = pattern.sub(lambda m: translate_dict[re.escape(m.group(0))], before_string)
    return after_string


def calculate_similarity(string1, string2):
    """
    替换申请人中无用的字符
    :return:
    """
    ignore_list = generate_ignore_character()
    ignore_pattern = ignore_list[0]
    translate_dict = ignore_list[1]
    
    string1 = replace_str(string1, ignore_pattern, translate_dict)
    string2 = replace_str(string2, ignore_pattern, translate_dict)
    seq = difflib.SequenceMatcher(None,string1,string2)
    ratio = seq.ratio()
    return ratio


def generate_translate_applicat_pattern(appliacat_list, appliacat_str):
    """
    将list中applicat转换为指定的名称
    :param appliacat_list:
    :return:
    """
    translate_dict = {items: appliacat_str for items in appliacat_list}
    translate_dict = dict((re.escape(key), value) for key, value in translate_dict.items())
    pattern = re.compile("|".join(translate_dict.keys()))
    return pattern



def delete_index_list(base_list, index_list):
    """
    根据index_list删除base_list中指定元素
    :param base_list:
    :param index_list:
    :return:
    """
    if base_list and index_list:
        return [base_list[i] for i in range(len(base_list)) if (i not in index_list)]
    
    
    
def save_inventor_applicat_dict(save_dict, save_name, caculate_type):
    """
        该函数用于保存统计不同申请人对应分类号的结果，
        :param base_class_nbr_dict 为计算的结果
        :param save_path 为保存的路径 eg:'f:/'
        :param save_name为保存的文件名
    """
    filePath = save_name + str(caculate_type) + '.txt'
    file = open(filePath, 'w')
    for name, class_nbr_dict in sorted(save_dict.items()):
        for class_nbr,class_nbr_count in sorted(class_nbr_dict.items()):
            dict_value = None
            dict_value = str(class_nbr) + ' ' + str(class_nbr_count)
            file.write(str(name) + ' ' + dict_value+ '\n')
    file.close()


