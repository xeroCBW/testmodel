# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = xiongliff
__mtime__ = '2020/1/12'
"""

# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = xiongliff
__mtime__ = '2019/9/23'
"""
from wangjingxue import const
from wangjingxue import utils
from utils import read_mat_data  as read_mat
import networkx as nx
import itertools
import numpy as np
import datetime


def get_inventor_params(base_data_array, file_name):
    """
    生成研发者对应专利数量，前向应用数量与被授权的年数，第一个专利到end_year的时间间隔
    研发者数据所在行数
    :param base_data_list:
    :return: 每个发明人的专利数量，如{'张三'：10, '李四'：12}
    """
    end_year = utils.get_end_year(file_name)
    inventor_list = get_all_inventor(base_data_array)
    # 统计专利数量
    inventor_patents_count_dict = {inventor: None for inventor in inventor_list}
    # 统计前向引用/授权时间
    inventor_patents_label_dict = {inventor: list() for inventor in inventor_list}
    # 统计
    inventor_pantents_bwt_dict = {inventor: list() for inventor in inventor_list}
    inventor_patents_rows_dict = {inventor: list() for inventor in inventor_list}
    # 每行的索引位置
    row_index = 0
    for row_data in base_data_array:
        # 读取申请人所在列
        inventor_value = row_data[const.INVENTOR_COL]
        # 读取前向应用数量列
        forward_cite_cnt = row_data[const.FORWARD_CITE_COL]
        
        if forward_cite_cnt is None:
            forward_cite_cnt = 0
        else:
            forward_cite_cnt = int(forward_cite_cnt)
        if end_year > int(row_data[const.GRANT_YEAR_COL]):
            # 被授权的年数 = grant_year - app_year
            grant_year_cnt = int(row_data[const.GRANT_YEAR_COL]) - int(row_data[const.APP_YEAR_COL])
        else:
            grant_year_cnt = end_year - int(row_data[const.APP_YEAR_COL])
        # 为了避免grant_year_cnt为0，做特殊处理
        
        if grant_year_cnt == 0:
            avg = (forward_cite_cnt + 0.0) / 1
        else:
            avg = (forward_cite_cnt + 0.0) / grant_year_cnt
        
        if inventor_value:
            inventor_value_list = inventor_value.split(",")
            
            for inventor in inventor_value_list:
                if inventor_patents_count_dict[inventor] is None:
                    inventor_patents_count_dict[inventor] = 1
                else:
                    inventor_patents_count_dict[inventor] += 1
                
                inventor_patents_label_dict[inventor].append(avg)
                
                inventor_pantents_bwt_dict[inventor].append(end_year - int(row_data[const.APP_YEAR_COL]))
                
                inventor_patents_rows_dict[inventor].append(row_index)
        
        row_index = row_index + 1
    # 计算截止到t年，研发者自申请到第一个专利的年数
    inventor_first_patent_dict = {inventor: np.max(inventor_pantents_bwt_dict[inventor]) for inventor in
                                  inventor_pantents_bwt_dict}
    return [inventor_patents_count_dict, inventor_patents_label_dict, inventor_first_patent_dict,
            inventor_patents_rows_dict]


def calculate_inv_perf(inventor_patents_count_dict, inventor_patents_label_dict, inventor_patents_bwt_dict):
    """
    计算创造力
    :param base_data_array:
    :param file_name:
    :return:
    """
    result_dict = dict()
    for inventor in inventor_patents_count_dict:
        if inventor_patents_bwt_dict[inventor] == 0:
            inventor_patents_bwt_dict[inventor] = 1
        result_dict[inventor] = inventor_patents_count_dict[inventor] * np.sum(inventor_patents_label_dict[inventor]) / \
                                inventor_patents_bwt_dict[inventor]
    return result_dict


def get_key_inventor(base_data_array, file_name):
    """
    获取关键研发者，创造力指数大于均值一个标准差
    :param base_data_array:
    :param file_name:
    :return:
    """
    inventor_var_list = get_inventor_params(base_data_array, file_name)
    key_inventor_list = list()
    inventor_patents_count_dict = inventor_var_list[0]
    inventor_patents_label_dict = inventor_var_list[1]
    inventor_patents_bwt_dict = inventor_var_list[2]
    inventor_inv_perf_dict = calculate_inv_perf(inventor_patents_count_dict, inventor_patents_label_dict,
                                                inventor_patents_bwt_dict)
    # 均值和标准差
    inventor_inv_perf_list = inventor_inv_perf_dict.values()
    if len(inventor_inv_perf_list) == 0:
        print(file_name)
    avg_inv_perf = np.mean(inventor_inv_perf_list)
    std_inv_perf = np.std(inventor_inv_perf_list)
    for inventor in inventor_inv_perf_dict:
        if inventor_inv_perf_dict[inventor] - avg_inv_perf > std_inv_perf:
            key_inventor_list.append(inventor)
    return key_inventor_list


def get_key_inventor_partner(base_data_array, inventor_patents_rows_dict, key_inventor):
    """
    获取关键研发者对应所有的合作者list
    :param base_data_array:
    :param inventor_patents_rows_dict:
    :param key_inventor:
    :return:
    """
    inventor_data_rows = inventor_patents_rows_dict[key_inventor]
    partner_set = set()
    for row_index in inventor_data_rows:
        row_data = base_data_array[row_index]
        # 读取申请人所在列
        inventor_value = row_data[const.INVENTOR_COL]
        if inventor_value:
            inventor_value_list = inventor_value.split(",")
            for inventor in inventor_value_list:
                partner_set.add(inventor)
    return list(partner_set)


def calculate_key_inventor_hole_label(base_data_array, inventor_patents_rows_dict, key_inventor):
    """
    计算关键研发者结构洞指数与中心度
    :param base_data_array:原始数据
    :param inventor_patents_count_dict: 用上一步的结果，用于获取所有节点
    :return:
    """
    
    inventor_data_rows = inventor_patents_rows_dict[key_inventor]
    # 获取关键研发者自我中心网中所有节点
    network_node_list = get_key_inventor_partner(base_data_array, inventor_patents_rows_dict, key_inventor)
    # 初始化无向网络
    key_inventor_network = nx.Graph()
    # 向网络中加入节点
    key_inventor_network.add_nodes_from(network_node_list)
    # 向网络中增加边的连线
    for row_index in inventor_data_rows:
        row_data = base_data_array[row_index]
        # 读取申请人所在列
        inventor_value = row_data[const.INVENTOR_COL]
        if inventor_value:
            inventor_value_list = inventor_value.split(",")
            if inventor_value_list and len(inventor_value_list) > 1:
                # 从inventor_value_list中获取所有2个研发者的组合
                for inventor_partner_array in itertools.combinations(inventor_value_list, 2):
                    key_inventor_network.add_edge(inventor_partner_array[0], inventor_partner_array[1])

    # 获取对应节点的度
    key_inventor_degree = key_inventor_network.degree(key_inventor)
    if key_inventor_degree == 0:
        hole_effi = const.ALONE_NODE_HOLE_EFFI
    else:
        hole_effi = nx.effective_size(key_inventor_network)[key_inventor] / key_inventor_degree
    return [hole_effi, key_inventor_degree]


def calculate_class_number_patent_count_dict(class_number_value, class_number_dict):
    """
    统计一条记录中分类号中的专利数量，并添加到class_number_dict中
    :param class_number_value:
    :param class_number_dict:
    :param calculate_type:
    :return:
    """
    class_number_string_list = utils.split_sub_class_string(class_number_value)

    # 去重
    class_nbr_list = list(set(class_number_string_list))
    for class_nbr in class_nbr_list:
        # 判断是否有该分类号
        if class_nbr in class_number_dict.keys():
            class_number_dict[class_nbr] += 1
        else:
            class_number_dict[class_nbr] = 1


def calculate_depth_breath_knowledge(base_data_array, inventor_patents_rows_dict, key_inventor):
    """
    计算研发者的知识深度
    :param base_data_array:
    :param inventor_patents_rows_dict:
    :param key_inventor:
    :return:
    """
    inventor_data_rows = inventor_patents_rows_dict[key_inventor]
    class_number_dict = dict()
    
    for row_index in inventor_data_rows:
        row_data = base_data_array[row_index]
        class_number_str = row_data[const.CLASS_NBR_COL]
        calculate_class_number_patent_count_dict(class_number_str, class_number_dict)
    class_number_patent_count_list = class_number_dict.values()
    
    pro_list = [(class_number_patent_count + 0.0) / len(inventor_data_rows) for class_number_patent_count in
                class_number_patent_count_list]
    avg_pro = np.mean(pro_list)
    std_pro = np.std(pro_list)
    knowledge_depth = std_pro / avg_pro
    knowledge_breath = len(class_number_dict.keys())
    return [knowledge_depth, knowledge_breath]


def get_key_inventor_contacts_list(base_data_array, file_name, inventor_patents_rows_dict, key_inventor,
                                   window_lenth=3):
    """
    获取关键研发者中的联系人
    :param base_data_array:
    :param inventor_patents_rows_dict:
    :param key_inventor:
    :return:
    """
    end_year = utils.get_end_year(file_name)
    key_inventor_partner = get_key_inventor_partner(base_data_array, inventor_patents_rows_dict, key_inventor)
    inventor_data_rows = inventor_patents_rows_dict[key_inventor]
    except_partner_list = list()
    for row_index in inventor_data_rows:
        row_data = base_data_array[row_index]
        if end_year - row_data[const.APP_YEAR_COL] <= window_lenth:
            # 3年内合作过的研发者
            inventor_value = row_data[const.INVENTOR_COL]
            if inventor_value:
                inventor_value_list = inventor_value.split(",")
                if inventor_value_list:
                    except_partner_list.extend(inventor_value_list)
    # 去重
    except_partner_list = list(set(except_partner_list))
    # 求except_partner_list与key_inventor_partner的差集
    return list(set(key_inventor_partner) ^ set(except_partner_list))


def calculate_contacts_depth_breath_knowledge(base_data_array, file_name, inventor_patents_rows_dict, key_inventor,
                                              window_length=3):
    """
    计算关键研发者联系人知识深度与宽度
    :param base_data_array:
    :param file_name:
    :param inventor_patents_rows_dict:
    :param key_inventor:
    :param window_lenth:
    :return:
    """
    contacts_list = get_key_inventor_contacts_list(base_data_array, file_name, inventor_patents_rows_dict, key_inventor,
                                                   window_length)
    contacts_depth_knowledge = list()
    contacts_breath_knowledge = list()
    if contacts_list:
        for contact in contacts_list:
            [knowledge_depth, knowledge_breath] = calculate_depth_breath_knowledge(base_data_array,
                                                                                   inventor_patents_rows_dict, contact)
            contacts_depth_knowledge.append(knowledge_depth)
            contacts_breath_knowledge.append(knowledge_breath)
        
        contacts_depth_knowledge_avg = np.mean(contacts_depth_knowledge)
        contacts_breath_knowledge_avg = np.mean(contacts_breath_knowledge)
    else:
        contacts_depth_knowledge_avg = None
        contacts_breath_knowledge_avg = None
    return [len(contacts_list), contacts_depth_knowledge_avg, contacts_breath_knowledge_avg]


def calculate_key_inventor_tie_strength(base_data_array, inventor_patents_rows_dict, key_inventor):
    """
    计算关键研发者自我中心网中的平均关系强度
    :param base_data_array:
    :param inventor_patents_rows_dict:
    :param key_inventor:
    :return:
    """
    inventor_data_rows = inventor_patents_rows_dict[key_inventor]
    inventor_cooper_nbr_dict = dict()
    for row_index in inventor_data_rows:
        row_data = base_data_array[row_index]
        # 读取申请人所在列
        inventor_value = row_data[const.INVENTOR_COL]
        if inventor_value:
            inventor_value_list = inventor_value.split(",")
            if inventor_value_list and len(inventor_value_list) > 1:
                # 从inventor_value_list中获取所有2个研发者的组合
                for inventor_partner_array in itertools.combinations(inventor_value_list, 2):
                    # 拼接合作关系的key,用于统计合作次数,按照从小到大拼接
                    if inventor_partner_array[0] < inventor_partner_array[1]:
                        inventor_cooper_key = inventor_partner_array[0] + '_' + inventor_partner_array[1]
                    else:
                        inventor_cooper_key = inventor_partner_array[1] + '_' + inventor_partner_array[0]
                    if inventor_cooper_key in inventor_cooper_nbr_dict.keys():
                        inventor_cooper_nbr_dict[inventor_cooper_key] += 1
                    else:
                        inventor_cooper_nbr_dict[inventor_cooper_key] = 1
    
    inventor_cooper_nbr_list = inventor_cooper_nbr_dict.values()
    if inventor_cooper_nbr_list:
        return np.mean(inventor_cooper_nbr_list)
    else:
        return 0


def get_all_inventor(base_data_all):
    """
    获取所有的研发者list
    :param base_data_all:
    :return:
    """
    inventor_set = set()
    for row_data in base_data_all:
        inventor_value = row_data[const.INVENTOR_COL]
        if inventor_value:
            inventor_value_list = inventor_value.split(",")
            for inventor in inventor_value_list:
                inventor_set.add(inventor)
    return list(inventor_set)


def get_first_patent_year(base_data_all):
    """
    从所有数据中获取每个研发者第一次生气专利的时间
    :param base_data_all:
    :return:
    """
    inventor_list = get_all_inventor(base_data_all)
    inventor_first_year_dict = {inventor: None for inventor in inventor_list}
    
    inventor_year_dict = {inventor: list() for inventor in inventor_list}
    for row_data in base_data_all:
        # 截取年份
        application_date_year = row_data[const.APP_YEAR_COL]
        inventor_value = row_data[const.INVENTOR_COL]
        if inventor_value:
            inventor_value_list = inventor_value.split(",")
            for inventor in inventor_value_list:
                inventor_year_dict[inventor].append(application_date_year)
    
    for inventor in inventor_year_dict:
        inventor_first_year_dict[inventor] = np.min(inventor_year_dict[inventor])
    return inventor_first_year_dict


def get_key_inventor_career_age(base_data_array, inventor_patents_rows_dict, key_inventor, inventor_first_year_dict):
    """
    获取关键研发者第一次申请专利到时间窗口内每一个专利的时间跨度，取平均数
    :param base_data_array:
    :param inventor_patents_rows_dict:
    :param key_inventor:
    :param inventor_first_year_dict:
    :return:
    """
    inventor_data_rows = inventor_patents_rows_dict[key_inventor]
    first_year = inventor_first_year_dict[key_inventor]
    career_age_list = list()
    for row_index in inventor_data_rows:
        row_data = base_data_array[row_index]
        application_date_year = row_data[const.APP_YEAR_COL]
        if application_date_year is None or first_year is None:
            career_age = 0
        else:
            career_age = application_date_year - first_year
        career_age_list.append(career_age)
    if career_age_list:
        return np.mean(career_age_list)
    else:
        return 0


def calculate_individual_quality(base_data_all, observe_year, inventor):
    """
    用于计算研发者的个人能力，观测年已申请到的专利数
    :param base_data_all:
    :param observe_year:
    :param inventor:
    :return:
    """
    individual_quality = 0
    for row_data in base_data_all:
        # 截取年份
        application_date_year = row_data[const.APP_YEAR_COL]
        inventor_value = row_data[const.INVENTOR_COL]
        if inventor_value:
            inventor_value_list = inventor_value.split(",")
            if inventor in inventor_value_list and application_date_year <= observe_year:
                individual_quality += 1
    return individual_quality


def calculate_mobility(base_data_array, inventor_patents_rows_dict, key_inventor):
    """
    计算上次成功申请专利后是否更换企业。若是则为1，或不是则为0
    :param base_data_array:
    :param inventor_patents_rows_dict:
    :param key_inventor:
    :return:
    """
    inventor_data_rows = inventor_patents_rows_dict[key_inventor]
    firm_set = set()
    for row_index in inventor_data_rows:
        row_data = base_data_array[row_index]
        firm_id = row_data[const.FIRM_COL]
        firm_set.add(firm_id)
    if len(firm_set) > 1:
        return 1
    else:
        return 0


if __name__ == '__main__':
    r1 = datetime.datetime.now()
    data = read_mat.read_base_data('D:/test.mat', True)
    r2 = datetime.datetime.now()
    print(r2 - r1)
    data_array = np.load('d:\\1993_2002.npy', allow_pickle=True)
    r3 = datetime.datetime.now()
    print(r3 - r2)
    data_name_str = 'd:\\1993_2002.npy'
    t1 = datetime.datetime.now()
    aa = get_all_inventor(data)
    t2 = datetime.datetime.now()
    print(t2 - t1)
    inventor_first_year_dict = get_first_patent_year(data)
    t3 = datetime.datetime.now()
    print(t3 - t2)