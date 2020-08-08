# -*- coding: utf-8 -*-
from __future__ import division
from collections import Counter
from common import const
from utils import split_class_nbr
from utils import count_patents
import numpy as np

def generate_class_nbr_count_dict(base_data_list, calculate_type):
    """
        将读取的excel文件list根据计算方式统计分类号出现的次数
        :param base_data_list 表示读取的excel文件list
        :param calculate_type 表示计算方式,，int型1,2,3
        :return:分类号计数字典，如{'G02F': 2, 'G02B': 3}
    """
    class_number_dict = dict()
    for base_data in base_data_list:
        class_number_value = base_data[const.CLASS_NBR]
        # 判断是否为字符串类型并且不能为空或者空字符串
        if isinstance(class_number_value, basestring) and class_number_value.strip() != "":
            # 根据分号进行切割
            class_number_value_list = class_number_value.split(";")
            # 判断list是否为空
            if class_number_value_list:
                for inx, class_nbr_string in enumerate(class_number_value_list):
                    # 按照不同的方式截取分类号
                    class_number = split_class_nbr.split_by_type(class_nbr_string, calculate_type)
                    # 判断字典中是否存在键，如果不存在则插入，存在则更新值+=1
                    if class_number in class_number_dict.keys():
                        class_number_dict[class_number] += 1
                    else:
                        class_number_dict[class_number] = 1
    return class_number_dict


def generate_inventor_class_nbr_count_dict(base_data_list, caculate_type):
    """
    计算base_data_list中不同发明人的分类号个数
    :param base_data_list:
    :param caculate_type: caculate_type 表示计算方式,，int型1,2,3
    :return: 不同发明人的分类号个数字典，如{'张三'：{'G02F': 2, 'G02B': 3}, '李四'： {'G02F': 2, 'G02B': 3}}
    """

    result_dict = {}
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
                            result_dict[inventor] = calculate_class_number_dict(class_number_value,
                                                                                {}, caculate_type)
                        else:
                            inventor_class_nbr_dict = result_dict[inventor]
                            result_dict[inventor] = calculate_class_number_dict(class_number_value,
                                                                                inventor_class_nbr_dict, caculate_type)
    return result_dict


def generate_applicant_class_nbr_count_dict(base_data_list, calculate_type):
    """
    计算base_data_list中不同发明人的分类号个数
    :param base_data_list:
    :param calculate_type: caculate_type 表示计算方式,，int型1,2,3
    :return: 不同申请人的分类号个数字典，如{'京东方'：{'G02F': 2, 'G02B': 3}, '星辰'： {'G02F': 2, 'G02B': 3}}
    """
    result_dict = {}
    for base_data in base_data_list:
        # 读取申请人所在列
        applicant_value = base_data[const.APPLICANT]
        # 读取分类号所在列
        class_number_value = base_data['CLASS_NBR']
        if isinstance(applicant_value, basestring) and applicant_value.strip() != "":
            applicant_list = applicant_value.split(";")
            if applicant_list:
                for applicant in applicant_list:
                    # 判断dict中是否存在该申请人，存在则更新，不存在则插入
                    if applicant not in result_dict.keys():
                        result_dict[applicant] = calculate_class_number_dict(class_number_value,
                                                                             {}, calculate_type)
                    else:
                        applicant_class_nbr_dict = result_dict[applicant]
                        result_dict[applicant] = calculate_class_number_dict(class_number_value,
                                                                             applicant_class_nbr_dict, calculate_type)
    return result_dict


def generate_inventor_class_nbr_patent_count_dict(base_data_list, caculate_type):
    """
    计算base_data_list中不同发明人的分类号对应的专利数量个数
    :param base_data_list:
    :param caculate_type: caculate_type 表示计算方式,，int型1,2,3
    :return: 不同发明人的分类号对应的专利数量字典，如{'张三'：{'G02F': 2, 'G02B': 3}, '李四'： {'G02F': 2, 'G02B': 3}}
    """

    result_dict = {}
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
                            result_dict[inventor] = count_patents.calculate_class_number_patent_count_dict(class_number_value,
                                                                                             {},
                                                                                             caculate_type)
                        else:
                            inventor_class_nbr_dict = result_dict[inventor]
                            result_dict[inventor] = count_patents.calculate_class_number_patent_count_dict(class_number_value,
                                                                                             inventor_class_nbr_dict,
                                                                                             caculate_type)
    return result_dict


def generate_applicant_class_nbr_patent_count_dict(base_data_list, calculate_type):
    """
    计算base_data_list中不同公司的分类号对应的专利数量个数
    :param base_data_list:
    :param caculate_type: caculate_type 表示计算方式,，int型1,2,3
    :return: 不同发明人的分类号对应的专利数量字典，如{'张三'：{'G02F': 2, 'G02B': 3}, '李四'： {'G02F': 2, 'G02B': 3}}
    """

    result_dict = {}
    for base_data in base_data_list:
        # 读取申请人所在列
        applicant_value = base_data[const.APPLICANT]
        # 读取分类号所在列
        class_number_value = base_data[const.CLASS_NBR]
        if isinstance(applicant_value, basestring) and applicant_value.strip() != "":
            applicant_list = applicant_value.split(";")
            if applicant_list:
                    for applicant in applicant_list:
                        # 判断dict中是否存在该申请人，存在则更新，不存在则插入
                        if applicant not in result_dict.keys():
                            result_dict[applicant] = count_patents.calculate_class_number_patent_count_dict(class_number_value,
                                                                                {}, calculate_type)
                        else:
                            applicant_class_nbr_dict = result_dict[applicant]
                            result_dict[applicant] = count_patents.calculate_class_number_patent_count_dict(class_number_value,
                                                                                applicant_class_nbr_dict, calculate_type)
    return result_dict



def calculate_class_number_dict(class_number_value, class_number_dict, calculate_type):
    """
    根据计算方式把分类号字符串切割后添加到class_number_dict中,
    注：这里没有同一条中分类号去重，即如果一条记录中如果有分类号：f01c/11,f01c/12,统计时是按f01c：2
    :param class_number_value: 分类号字符串
    :param class_number_dict: 分类号字典，其中键为分类号，值为出现的次数
    :param calculate_type: 计算方式，int型1,2,3其中:1.子分类号G02F,2.子分类号G02F1,3.G02F1/133
    :return:分类号计数字典，如{'G02F': 2, 'G02B': 3}
    """
    if isinstance(class_number_value, basestring) and class_number_value.strip() != "":
        class_number_string_list = class_number_value.split(";")
        if class_number_string_list:
            for class_nbr_string in class_number_string_list:
                class_nbr = split_class_nbr.split_by_type(class_nbr_string, calculate_type)
                # 判断是否有该分类号
                if class_nbr in class_number_dict.keys():
                    class_number_dict[class_nbr] += 1
                else:
                    class_number_dict[class_nbr] = 1
    return class_number_dict


def calculate_class_number_career_count_dict(base_data, class_number_dict, calculate_type):
    """
    计算拥有不同分类号数量的员工数量
    :param class_number_dict: 分类号字典，其中键为分类号，值为出现的次数
    :param calculate_type: 计算方式，int型1,2,3其中:1.子分类号G02F,2.子分类号G02F1,3.G02F1/133
    :return:分类号计数字典，如{'G02F': 2, 'G02B': 3}
    """
    class_number_value = base_data[const.CLASS_NBR]
    inventor_value = base_data[const.INVENTOR]
    #计算每一行中员工数量
    if isinstance(inventor_value, basestring) and inventor_value.strip() != "":
        inventor_string_list = inventor_value.split(";")
    
    if isinstance(class_number_value, basestring) and class_number_value.strip() != "":
        class_number_string_list = class_number_value.split(";")
        if class_number_string_list:
            for class_nbr_string in class_number_string_list:
                class_nbr = split_class_nbr.split_by_type(class_nbr_string, calculate_type)
                # 判断是否有该分类号
                if class_nbr in class_number_dict.keys():
                    class_number_dict[class_nbr] += len(inventor_string_list)
                else:
                    class_number_dict[class_nbr] = len(inventor_string_list)
    return class_number_dict




def caculate_knowledg_breadth_1(base_data_list, caculate_type):
    """
    第一种计算知识宽度的方式
    :param inventor_class_number_dict:
    :return:
    """
    inventor_class_number_dict = generate_inventor_class_nbr_count_dict(base_data_list, caculate_type)
    result_dict = dict()
    for name, class_nbr_dict in inventor_class_number_dict.items():
        result_dict[name] = len(class_nbr_dict.keys())
    return result_dict


def caculate_knowledg_breadth_2(base_data_list, calculate_type):
    """
    第二种计算知识宽度的方式
    :param base_data_list:
    :param caculate_type:
    :return:
    """
    #获取每个发明人对应的分类号所占有的专利数量dict
    inventor_class_number__patent_count_dict = generate_inventor_class_nbr_patent_count_dict(base_data_list, calculate_type)
    result_dict =dict()
    if inventor_class_number__patent_count_dict:
        for inventor,class_nbr_patent_cnt_dict in inventor_class_number__patent_count_dict.items():
            if class_nbr_patent_cnt_dict:
                sum_patent_cnt = sum(class_nbr_patent_cnt_dict.values())
                knowledge_breadth = float()
                for class_nbr, patent_cnt in class_nbr_patent_cnt_dict.items():
                    knowledge_breadth += pow(patent_cnt/sum_patent_cnt,2)
                result_dict[inventor] = knowledge_breadth
    return result_dict



def caculate_campany_knowledge_breadth(base_data_list, calculate_type, start_time, end_time):
    """
    计算每一家公司对应的知识宽度
    :param start_year:
    :param end_year:
    :return:
    """
    row_data_list = list()
    return_dict = dict()
    for row_data in base_data_list:
        if row_data['APPLY_DATE'] >= start_time and row_data['APPLY_DATE'] <= end_time:
            row_data_list.extend(row_data)
    applicant_class_nbr_dict = generate_applicant_class_nbr_count_dict(base_data_list,calculate_type)
    for applicant, class_nbr_dict in applicant_class_nbr_dict.items():
        return_dict[applicant] = class_nbr_dict.len(class_nbr_dict)

    return return_dict


def caculate_inventor_knowedge_deepth(base_data_list, calculate_type):
    # 每个研发员在技术分类ｔ上专利数占所有企业在技术分类ｔ上专利数的比例
    inventor_result = dict()
    inventor_class_nbr_dict = generate_inventor_class_nbr_patent_count_dict(base_data_list,calculate_type)
    
    #计算所有研发者分类号对应的专利数量
    all_inventor_class_nbr_patent_cnt_dict = dict()
    for inventor, class_nbr_dict in inventor_class_nbr_dict.items():
        all_inventor_class_nbr_patent_cnt_dict = dict(Counter(all_inventor_class_nbr_patent_cnt_dict) +
                                                      Counter(class_nbr_dict))
    #计算所有数据中每个分类号对应的专利数量
    class_nbr_patent_cnt_dict = count_patents.count_class_nbr_patent_cnt(base_data_list, calculate_type)
    for inventor, class_nbr_dict in inventor_class_nbr_dict.items():
        class_nbr_rate_list = list()
        for class_nbr, patent_cnt in class_nbr_dict.items():
            class_nbr_patent_cnt = class_nbr_patent_cnt_dict[class_nbr]
            class_nbr_rate_element = patent_cnt / class_nbr_patent_cnt
            class_nbr_rate_denominator = all_inventor_class_nbr_patent_cnt_dict[class_nbr] / len(base_data_list)
            class_nbr_rate_list.append(class_nbr_rate_element / class_nbr_rate_denominator)
        #计算均值和标准差
        avg = np.mean(class_nbr_rate_list)
        std = np.std(class_nbr_rate_list)
        knowledge_deepth = avg / std
        inventor_result[inventor] = knowledge_deepth
    return inventor_result


def caculate_company_knowedge_deepth(base_data_list, calculate_type):
    # 每个公司在技术分类ｔ上专利数占所有企业在技术分类ｔ上专利数的比例
    applicant_result = dict()
    applicant_class_nbr_dict = generate_applicant_class_nbr_patent_count_dict(base_data_list, calculate_type)
    # 计算所有公司分类号对应的专利数量
    all_applicant_class_nbr_patent_cnt_dict = dict()
    for applicant, class_nbr_dict in applicant_class_nbr_dict.items():
        all_applicant_class_nbr_patent_cnt_dict = dict(Counter(all_applicant_class_nbr_patent_cnt_dict) +
                                                       Counter(class_nbr_dict))
    # 计算所有数据中每个分类号对应的专利数量
    class_nbr_patent_cnt_dict = count_patents.count_class_nbr_patent_cnt(base_data_list, calculate_type)
    for applicant, class_nbr_dict in applicant_class_nbr_dict.items():
        class_nbr_rate_list = list()
        for class_nbr, patent_cnt in class_nbr_dict.items():
            class_nbr_patent_cnt = class_nbr_patent_cnt_dict[class_nbr]
            class_nbr_rate_element = patent_cnt / class_nbr_patent_cnt
            class_nbr_rate_denominator = all_applicant_class_nbr_patent_cnt_dict[class_nbr] / len(base_data_list)
            class_nbr_rate_list.append(class_nbr_rate_element / class_nbr_rate_denominator)
        # 计算均值和标准差
        avg = np.mean(class_nbr_rate_list)
        std = np.std(class_nbr_rate_list)
        knowledge_deepth = avg / std
        applicant_result[applicant] = knowledge_deepth
    return applicant_result


def calculate_knowledge_storage(base_data_list, calculate_type):
    """
    计算知识存量，没有使用阶段的参数，只计算在每个公司中拥有不同分类号的人数和
    :param base_data_list:
    :param calculate_type:
    :return:
    """
    result_dict = {}
    for base_data in base_data_list:
        # 读取申请人所在列
        applicant_value = base_data[const.applicant]
        if isinstance(applicant_value, basestring) and applicant_value.strip() != "":
            applicant_list = applicant_value.split(";")
            if applicant_list:
                for applicant in applicant_list:
                    # 判断dict中是否存在该申请人，存在则更新，不存在则插入
                    if applicant not in result_dict.keys():
                        result_dict[applicant] = calculate_class_number_career_count_dict(base_data, {}, calculate_type)
                    else:
                        applicant_class_nbr_dict = result_dict[applicant]
                        result_dict[applicant] = calculate_class_number_career_count_dict(base_data,
                                                                                          applicant_class_nbr_dict,
                                                                                          calculate_type)
    return result_dict


def save_class_nbr_dict(class_nbr_dict, save_name, caculate_type):
    """
        该函数用于保存分类号的三种计算方式的结果，
        :param base_class_nbr_list 为计算的结果
        :param save_path 为保存的路径 eg:'f:/'
        :param save_name 为保存的文件名
        base_class_nbr_dict3
    """
    filePath = save_name+str(caculate_type)+'.txt'
    file = open(filePath, 'w')
    for class_nbr, class_nbr_count in sorted(class_nbr_dict.items()):
        file.write(str(class_nbr)+' '+str(class_nbr_count)+'\n')
    file.close()


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


if __name__ == '__main__':
    pass
    #示例：base_class_nbr_list对应1的统计结果，files表示excel文件的地址，测试地址为r'f:\test1.xls'，更改excel文件时时修改''内的内容即可
    #save_base_class_nbr_list保存对应的计算结果到txt文件，三种计算方式分别对应文件名1.txt，文件名2.txt,文件名3.txt
    #使用时放开##########下的两行，对应需求文档1的需求
    #################################################################
    #base_class_nbr_list = calculate_class_nbr(files=r'f:\test.xls')
    #save_base_class_nbr_list(base_class_nbr_list,'f:/','base_class_nbr_list')
    #################################################################
    #示例：用于计算并保存不同申请人对应的分类号统计结果，其中需求2对应不同的发明人，则将applicat_col设置为8（excel的第6列，从0开始）
    #需求3对应不同的申请人，则将applicat_col设置为6,（excel的第6列）
    #3种不同的统计方式，则将caculate_type设置为1,2,3
    #保存为f:/xw.txt,如需修改，则更改save_path和save_name
    #dict_temp1 = caculate_applicat(files=r'f:\test.xls',caculate_type=3,applicat_col=8)
    #save_class_nbr_dict(dict_temp1,save_path="f:/",save_name="xw")



