# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = xiongliff
__mtime__ = '2019/7/20'
"""
import matplotlib.pyplot as plt
from common import const
from utils import split_class_nbr

def calculte_class_nbr_rate(base_data_list, calculate_type):
    """
    生成不同方式切割分类号后， 每个分类号在所有专利的平均权重
    其中一个专利中第一个分类号占权重为：rate1 = 1 / 分类号数量 + (1-1 / 分类号数量) * 0.5
    如果超过一个专利，则其他的权重都为：rate2 = (1-rate1)/(分类号数量-1)
    遍历所有专利然后求每个分类的权重均值
    :param base_data_list:
    :param calculate_type:
    :return:
    """
    class_number_dict = {}
    for base_data in base_data_list:
        # 读取分类号所在列
        class_number_value = base_data[const.CLASS_NBR]
        if isinstance(class_number_value, basestring) and class_number_value.strip() != "":
            class_number_string_list = class_number_value.split(";")
            if class_number_string_list:
                # 取出分类号组成新的list
                class_nbr_list = [split_class_nbr.split_by_type(class_nbr_string, calculate_type) for class_nbr_string
                                  in class_number_string_list]
                # 按顺序去重
                sort_class_nbr_list = list(set(class_nbr_list))
                sort_class_nbr_list.sort(key=class_nbr_list.index)
                # 计算一行中分类号的权重
                # 第一个的分类号的权重
                row_rate = 1 / len(sort_class_nbr_list) + (1 - 1 / len(sort_class_nbr_list)) * 0.5
                if len(sort_class_nbr_list) > 1:
                    other_row_rate = (1 - row_rate) / (len(sort_class_nbr_list) - 1)
                for index, name in enumerate(sort_class_nbr_list):
                    if index == 0:
                        # 判断是否有该分类号
                        if sort_class_nbr_list[index] in class_number_dict.keys():
                            class_number_dict[sort_class_nbr_list[index]] += row_rate
                        else:
                            class_number_dict[sort_class_nbr_list[index]] = row_rate
                    else:
                        # 判断是否有该分类号
                        if sort_class_nbr_list[index] in class_number_dict.keys():
                            class_number_dict[sort_class_nbr_list[index]] += other_row_rate
                        else:
                            class_number_dict[sort_class_nbr_list[index]] = other_row_rate
    #对dict中所有数据除以专利数量
    patent_count = len(base_data_list) + 0.0
    class_number_dict = { key: value / patent_count for key,value in class_number_dict.items()}
    return class_number_dict

def generate_class_number_curve(class_number_dict):
    """
    使用plt画曲线时，由于x,y轴必须是list,所以需要对分类号对应的权重排序后，分别取出key,value对应的list
    :param class_number_dict:
    :return:
    """
    #按从大到小的顺序排序
    sort_list = sorted(class_number_dict.items(), key=lambda x: x[1], reverse=True)
    sort_class_nbr_list = [ unit[0] for unit in sort_list]
    sort_rate_list = [ unit[1] for unit in sort_list]
    return [sort_class_nbr_list, sort_rate_list]


def draw_class_number_curve(base_data_list):
    """
    使用plt画曲线，
    :param base_data_list:
    :return:
    """
    #取前3位统计的结果
    class_number_dict1 = calculte_class_nbr_rate(base_data_list, 4)
    class_number_curve_list1 = generate_class_number_curve(class_number_dict1)
    #取前4位统计的结果
    class_number_dict2 = calculte_class_nbr_rate(base_data_list, 1)
    class_number_curve_list2 = generate_class_number_curve(class_number_dict2)
    #取/号前的统计结果
    class_number_dict3 = calculte_class_nbr_rate(base_data_list, 2)
    class_number_curve_list3 = generate_class_number_curve(class_number_dict3)
    #开始画图
    fig, ax = plt.subplots()
    plt.title('Result Analysis')
    x1 = range(len(class_number_curve_list1[0]))
    x2 = range(len(class_number_curve_list2[0]))
    x3 = range(len(class_number_curve_list3[0]))
    plt.scatter(x1,class_number_curve_list1[1], color='black', label='1')
    plt.scatter(x2, class_number_curve_list2[1], color='red', label='2')
    plt.scatter(x3, class_number_curve_list3[1], color='blue', label='3')
    plt.xticks(x1, class_number_curve_list1[0], rotation=0)
    plt.xticks(x2, class_number_curve_list2[0], rotation=0)
    plt.xticks(x3, class_number_curve_list3[0], rotation=0)
    plt.xlabel('class_nbr')
    plt.ylabel('rate')
    plt.show()
