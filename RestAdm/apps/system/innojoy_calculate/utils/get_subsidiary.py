# -*- coding: utf-8 -*-
"""
__title__ = '获取子公司'
__author__ = xiongliff
__mtime__ = '2019/6/19'
"""
import re
from innojoy_calculate.utils import count_patents
from innojoy_calculate.utils import base_utils
from innojoy_calculate.utils import read_xls_data
from innojoy_calculate.common import const


def calculate_subsidiary(base_data_list):
    """
    获取申请人中的子公司
    
    思路：先统计所有公司的专利数量，按高低排序，专利数量大的意味该公司的研发实力强，
    越有可能是母公司，而母公司与子公司的名称相似度会更大，因此将专利数量大的公司作为基准公司，计算其子公司，
    然后将母公司与子公司过滤后，继续该循环，以此来获取子公司
    1.统计所有公司的专利数量，按高低排序 -> applicant_patents_dict
    2.从applicant_patents_dict中选出个数最多的作为基准申请人
    3.遍历applicant_patents_dict，比较keys去除无用字符，如地点名，公司，集团等后的相似度，相似度大的即为同一个公司
    4.从applicant_patents_dict中去除子公司后，继续循环计算，直至遍历结束
    
    :param base_data_list:
    :return:
    """
    #获取申请人专利数量
    count_applicant_patents = count_patents.count_applicant_patents_by_data(base_data_list)
    
    #根据专利数量排序
    sorted_applicant_patents_list = sorted(count_applicant_patents.items(), key=lambda x: x[1], reverse=True)
    sorted_applicant_patents_list = [applicant_patent[0] for applicant_patent in sorted_applicant_patents_list]
    subsidiary__dict = dict()
    #取出第一个
    while sorted_applicant_patents_list:
        base_applicant = sorted_applicant_patents_list[0]
        sorted_applicant_patents_list.pop(0)
        subsidiary__index_list = compare_applicant_similar(base_applicant, sorted_applicant_patents_list)
        if subsidiary__index_list:
            #存放母子公司对应dict
            subsidiary__dict[base_applicant] = [sorted_applicant_patents_list[index] for index in subsidiary__index_list]
            #在sorted_applicant_patents_list中删除子公司
            sorted_applicant_patents_list = base_utils.delete_index_list(sorted_applicant_patents_list, subsidiary__index_list)
    return subsidiary__dict

    
def compare_applicant_similar(applicant_string, applicant_patents_list):
    if applicant_patents_list:
        subsidiary__index_list = list()
        for index in range(len(applicant_patents_list)):
            applicant_similar = base_utils.calculate_similarity(applicant_string, applicant_patents_list[index])
            #相似度的阈值设为
            if applicant_similar >= 0.75:
                subsidiary__index_list.append(index)
        
        return subsidiary__index_list


def generate_subsidiary_data(subsidiary__dict):
    """
    根据subsidiary__dict生成替换子公司的正则表达式pattern和translate_dict
    :param subsidiary__dict:
    :return:
    """
    
    if subsidiary__dict:
        translate_dict = dict()
        for parent, subsidiary_list in subsidiary__dict.items():
            if subsidiary_list:
                for subsidiary in subsidiary_list:
                    translate_dict[subsidiary] = parent

        translate_dict = dict((re.escape(key), value) for key, value in translate_dict.items())
        pattern = re.compile("|".join(translate_dict.keys()))
        return [pattern, translate_dict]


def replace_subsidiary(base_data_list):
    """
    根据base_data_list将数据中子公司替换成母公司名称
    """
    subsidiary__dict = calculate_subsidiary(base_data_list)
    print(subsidiary__dict.keys())
    subsidiary_data = generate_subsidiary_data(subsidiary__dict)
    subsidiary_pattern = subsidiary_data[0]
    translate_dict = subsidiary_data[1]
    for base_data in base_data_list:
        base_data[const.APPLICANT] = base_utils.replace_str(base_data[const.APPLICANT],subsidiary_pattern,translate_dict)


if __name__ == '__main__':
    base_data_list = read_xls_data.read_data()
    replace_subsidiary(base_data_list)
