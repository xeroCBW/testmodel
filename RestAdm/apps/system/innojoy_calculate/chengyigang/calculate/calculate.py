# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = xiongliff
__mtime__ = '2019/7/20'
"""

from utils import read_xls_data
from common import const
from utils import split_class_nbr
from utils import count_patents
from chengyigang.calculate import calculate_unionfind


def calculate_class_nbr_similar(base_data_list1, calculate_type):
    """
    遍历所有专利，如果一个专利中分类号数量大于2，则将这个专利中任意2个分类号的组合作为计算结果dict中的key,
    然后计算所有专利中这个key对应的value
    :param base_data_list1: 基本的专利数据
    :param calculate_type: 分类号的切割方式
    :return:
    """
    # 先获取分类号对应专利数量dict
    class_number_patent_cnt_dict = count_patents.count_class_nbr_patent_cnt(base_data_list1, calculate_type)
    # 两个分类号对应的专利数量
    unique_class_number_patent_cnt_dict = count_patents.count_unique_class_nbr_patent_cnt(base_data_list1,
                                                                                          calculate_type)
    unique_class_number_dict = dict()
    # 计算相似度
    for unique_class_number, cnt in unique_class_number_patent_cnt_dict.items():
        # 将分类号切割
        unique_class_number_list = unique_class_number.split('#')
        unique_class_number1 = unique_class_number_list[0]
        unique_class_number2 = unique_class_number_list[1]
        rate_a_b = (cnt + 0.0) / class_number_patent_cnt_dict[unique_class_number1]
        rate_b_a = (cnt + 0.0) / class_number_patent_cnt_dict[unique_class_number2]
        similary_rate = rate_a_b + rate_b_a
        unique_class_number_dict[unique_class_number] = similary_rate
    return unique_class_number_dict


def generate_class_nbr_group(threshold, unique_class_number_dict):
    """
    根据相似度的阈值threshold来分组
    :param unique_class_number_dict:
    :param threshold: 阈值
    :return:
    """
    # 存放用于合并分组的分类号list
    merge_class_nbr_list = list()
    for unique_class_nbr, similary_rate in unique_class_number_dict.items():
        # 获取unique_class_number_dict中相似度大于threshold的分类号组合list
        if similary_rate >= threshold:
            merge_class_nbr = unique_class_nbr.split('#')
            merge_class_nbr_list.append(merge_class_nbr)
    # 通过并查集来计算分组
    unionfind_init_tree = calculate_unionfind.unionfind(merge_class_nbr_list)
    unionfind_init_tree.createtree()
    group_list = unionfind_init_tree.gettree()
    return group_list


def generate_all_class_nbr_group(base_data_list1, calculate_type, threshold):
    # 先获取分类号对应专利数量dict
    class_number_patent_cnt_dict = count_patents.count_class_nbr_patent_cnt(base_data_list1, calculate_type)
    # 所有分类号对应的list
    class_nbr_list = class_number_patent_cnt_dict.keys()
    # 获取可以分组的分类号list
    unique_class_number_dict = calculate_class_nbr_similar(base_data_list1, calculate_type)
    class_nbr_group_list = generate_class_nbr_group(threshold, unique_class_number_dict)
    # 获取不在class_nbr_group_list中的其他分类号，并添加到no_class_nbr_group_list中去
    no_class_nbr_group_list = list()
    for class_nbr in class_nbr_list:
        for class_nbr_group in class_nbr_group_list:
            if class_nbr not in class_nbr_group:
                no_class_nbr_group_list.append(class_nbr)
    # 合并
    class_nbr_group_list.extend(no_class_nbr_group_list)
    return class_nbr_group_list


def calculate_class_number_group_patent_count_dict(class_number_value, class_number_dict, calculate_type,
                                                   class_nbr_group_list):
    """
    统计一条记录中各个分类号按照class_mbr_group_list中的分组后在每一组中的专利数量，并添加到class_number_dict中
    :param class_number_value:
    :param class_number_dict:
    :param calculate_type:
    :param class_nbr_group_list:
    :return:
    """
    if isinstance(class_number_value, basestring) and class_number_value.strip() != "":
        class_number_string_list = class_number_value.split(";")
        if class_number_string_list:
            # 取出分类号组成新的list
            class_nbr_list = [split_class_nbr.split_by_type(class_nbr_string, calculate_type)
                              for class_nbr_string in class_number_string_list]
            # 去重
            class_nbr_list = list(set(class_nbr_list))
            # 判断分类号是不是已经属于一个组了，防止多计数
            # 比如a,b属于一个组，在计数时只应加1
            class_nbr_group_set =set()
            for class_nbr in class_nbr_list:
                key = None
                for class_nbr_group in class_nbr_group_list:
                    if class_nbr in class_nbr_group:
                        key = str(class_nbr_group)
                        break
                # 判断该分类号是否在class_nbr_group_set中有
                if not key in class_nbr_group_set:
                    if key in class_number_dict.keys():
                        class_number_dict[key] += 1
                    else:
                        class_number_dict[key] = 1
                    class_nbr_group_set.add(key)
    return class_number_dict
    
    
def calculate_inventor_class_nbr_group_count(base_data_list,calculate_type, group_list):
    """
    用于计算发明家与分类号分组的专利数量dict
    :param class_nbr_group_list:
    :param base_data_list:
    :param threshold:
    :param calculate_type:
    :return:
    """
    #统计发明人对应的在分类号分组下的专利数量dict
    result_dict = dict()
    for base_data in base_data_list:
        # 读取申请人所在列
        inventor_value = base_data[const.INVENTOR]
        # 读取分类号所在列
        class_number_value = base_data[const.CLASS_NBR]
        if isinstance(inventor_value, basestring) and inventor_value.strip() != "":
            inventor_list = inventor_value.split(";")
            if inventor_list:
                    for inventor in inventor_list:
                        # 判断dict中是否存在该申请人，存在则更新，不存在则插入
                        if inventor not in result_dict.keys():
                            result_dict[inventor] = calculate_class_number_group_patent_count_dict(class_number_value,
                                                                                                   {},
                                                                                                   calculate_type,
                                                                                                   group_list)
                        else:
                            inventor_class_nbr_dict = result_dict[inventor]
                            result_dict[inventor] = calculate_class_number_group_patent_count_dict(class_number_value,
                                                                                                   inventor_class_nbr_dict,
                                                                                                   calculate_type,
                                                                                                   group_list)
    return result_dict
    
    
def calculate_overlap_rate(inventor_class_nbr_group_count_dict):
    """
    计算交叠率
    :param inventor_class_nbr_group_patent_count:
    :return:
    """
    #发明家的总数
    inventor_cnt = len(inventor_class_nbr_group_count_dict.keys())
    #无法分组的发明家数量
    cant_group_inventor = 0
    for inventor, class_nbr_group_count_dict in inventor_class_nbr_group_count_dict.items():
        
        #如果在class_nbr_group_count_dict中对应max值的大于等于2个，则说明无法判断属于哪个分组
        #sort_list是按dict中的value排序后形成list
        #形如：[('g01',3),('g02',2)]
        #所以只需判断sort_list中第1,2个元素的value是否相等即可即sort_list[0][1] == sort_list[1][1]
        sort_list = sorted(class_nbr_group_count_dict.items(), key=lambda x: x[1], reverse=True)
        if len(sort_list) > 1 and not sort_list[0][1] == sort_list[1][1]:
            cant_group_inventor += 1
    #计算比值
    return (cant_group_inventor + 0.0) / inventor_cnt

def calculate_vacancy_rate(inventor_class_nbr_group_count_dict ,class_nbr_group_list):
    """
    计算空置率，由于inventor_class_nbr_group_count_dict统计的是每个发明者对应的在每个分组下的专利数量
    没有专利数量的分组，不会放入dict中，因此要求空置率，则遍历inventor_class_nbr_group_count_dict将每个发明者的对应的分类号分组，放入一个
    set中，然后计数set中哪些分类号没有，即可
    :param inventor_class_nbr_group_count_dict:
    :param class_nbr_list:
    :return:
    """
    exisit_class_group_set = set()
    no_inventor_class_nbr_group_cnt = 0
    for inventor, class_nbr_group_count_dict in inventor_class_nbr_group_count_dict.items():
        #获取有对应发明人的专利分组list
        class_nbr_group_count_dict_values = class_nbr_group_count_dict.keys()
        #放入set中
        exisit_class_group_set.update(set(class_nbr_group_count_dict_values))
    
    for class_nbr_group in class_nbr_group_list:
        if str(class_nbr_group) not in exisit_class_group_set:
            no_inventor_class_nbr_group_cnt += 1
    return (no_inventor_class_nbr_group_cnt + 0.0) / len(class_nbr_group_list)

def calculate_rate(base_data_list, threshold, calculate_type):
    """
    计算不同阈值下小组数量，交叠率，空集率
    :param base_data_list:
    :param threshold:
    :param calculate_type:
    :return:
    """
    result_dict = dict()
    group_list = generate_all_class_nbr_group(base_data_list, calculate_type, threshold)
    inventor_class_nbr_group_count_dict = calculate_inventor_class_nbr_group_count(base_data_list,calculate_type,
                                                                                   group_list)
    group_cnt = len(group_list)
    overlap_rate = calculate_overlap_rate(inventor_class_nbr_group_count_dict)
    vacancy_rate = calculate_vacancy_rate(inventor_class_nbr_group_count_dict,group_list)
    result_dict[threshold] = [group_cnt, overlap_rate, vacancy_rate]
    return result_dict
if __name__ == '__main__':
    
    base_data_list = read_xls_data.read_data()
    print(calculate_rate(base_data_list, 0.5, 1))