# -*- coding: utf-8 -*-
"""
__title__ = '画出类、大组、小组的树状曲线'
__author__ = xiongliff
__mtime__ = '2019/7/16'
"""
import json
import os
from innojoy_calculate.common import const
from innojoy_calculate.utils import read_xls_data

class Node:
    def __init__(self, id, value,is_leaf, parent_id):
        self.id =id
        self.value = value
        self.is_leaf = is_leaf
        self.parent_id = parent_id
    
    def get_value(self):
        return self.value
    
    def get_parent_id(self):
        return self.parent_id
    
    def get_id(self):
        return self.id
    
    def get_is_leaf(self):
        return self.is_leaf
    
    def add_value(self):
        self.value += 1


def generate_tree_node_data(base_data_list):
    """
    读取base_data_list，并按部、大类、小类、大组、小组生成对应的树状结构
    保存在dict中
    node中有id，即分类号，value即出现的次数，parent_id即上层的所属关系
    :param base_data_list:
    :return:
    """
    #存放{id:node}
    id_node_dict = dict()
    for base_data in base_data_list:
        # 读取分类号所在列
        class_number_value = base_data[const.CLASS_NBR]
        if isinstance(class_number_value, basestring) and class_number_value.strip() != "":
            class_number_string_list = class_number_value.split(";")
            if class_number_string_list:
                for class_nbr_string in class_number_string_list:
                    #部分类号取第一位
                    part_class_nbr = class_nbr_string[0]
                    #如果没有part_class_nbr则生成根节点，否则计数加1
                    if part_class_nbr not in id_node_dict.keys():
                        part_class_nbr_node = Node(part_class_nbr, 1, False, None)
                        id_node_dict[part_class_nbr] = part_class_nbr_node
                    else:
                        id_node_dict[part_class_nbr].add_value()
                    #大类分类号取第前3位
                    main_category_class_nbr = class_nbr_string[0:2]
                    # 如果没有main_category_class_nbr则生成节点，否则计数加1
                    if main_category_class_nbr not in id_node_dict.keys():
                        main_category_class_nbr_node = Node(main_category_class_nbr, 1, False, part_class_nbr)
                        id_node_dict[main_category_class_nbr] = main_category_class_nbr_node
                    else:
                        id_node_dict[main_category_class_nbr].add_value()
                    
                    #小类分类号取前4位
                    sub_category_class_nbr = class_nbr_string[0:3]
                    # 如果没有sub_category_class_nbr则生成节点，否则计数加1
                    if sub_category_class_nbr not in id_node_dict.keys():
                        sub_category_class_nbr_node = Node(sub_category_class_nbr, 1, False, main_category_class_nbr)
                        id_node_dict[sub_category_class_nbr] = sub_category_class_nbr_node
                    else:
                        id_node_dict[sub_category_class_nbr].add_value()
                    #大组分类号取/号前的
                    main_group_class_nbr = class_nbr_string.split("/")[0]
                    # 如果没有main_group_class_nbr则生成节点，否则计数加1
                    if main_group_class_nbr not in id_node_dict.keys():
                        main_group_class_nbr_node = Node(main_group_class_nbr, 1, False, sub_category_class_nbr)
                        id_node_dict[main_group_class_nbr] = main_group_class_nbr_node
                    else:
                        id_node_dict[main_group_class_nbr].add_value()
                    #小组分类号取（号前的
                    sub_group_class_nbr = class_nbr_string.split("(")[0]
                    # 如果没有sub_group_class_nbr则生成节点，否则计数加1
                    if sub_group_class_nbr not in id_node_dict.keys():
                        sub_group_class_nbr_node = Node(sub_group_class_nbr, 1, True, main_group_class_nbr)
                        id_node_dict[sub_group_class_nbr] = sub_group_class_nbr_node
                    else:
                        id_node_dict[sub_group_class_nbr].add_value()
                
    return id_node_dict

    
def generate_tree_display(id_node_dict):
    """
    根据id_node_dict生成指定展示所需的数据结构：
    {name:123,
     value:22
     childreen:[]
     }
    :param id_node_dict:
    :return:
    """
    node_list = id_node_dict.values()
    root_node_list = list()
    #先找到根节点，即parent_id为None的节点
    for node in node_list:
        if not node.get_parent_id():
            root_node = dict()
            root_node['name'] = node.get_id()
            root_node['value'] = node.get_value()
            root_node['children'] = list()
            root_node_list.append(root_node)
    for root_node in root_node_list:
        add_children_node(root_node, node_list)
    #如果len(root_node_list)>1,则加一个统一的根节点,否则只有一个根节点
    result_root_node = dict()
    if len(root_node_list) > 1:
        result_root_node['name'] = ''
        result_root_node['value'] = ''
        result_root_node['children'] = root_node_list
    else:
        result_root_node = root_node_list[0]
    return result_root_node

def add_children_node(root_node, node_list):
    for node in node_list:
        if node.get_parent_id() == root_node['name']:
            son_node = dict()
            son_node['name'] = node.get_id()
            son_node['value'] = node.get_value()
            if not node.get_is_leaf():
                son_node['children'] = list()
                add_children_node(son_node, node_list)
            root_node['children'].append(son_node)


def save_tree_data(base_base_data_list):
    id_node_dict = generate_tree_node_data(base_base_data_list)
    tree_data = generate_tree_display(id_node_dict)
    try:
        os.remove(const.JSON_PATH)
    except WindowsError:
        pass
    file = open(const.JSON_PATH,'w')
    file.write('display_tree = ')
    json.dump(tree_data, file, ensure_ascii=False)
    
    file.close()

if __name__ == '__main__':
    # root_node = dict()
    # root_node['name'] = 'B'
    # root_node['value'] = 12
    # root_node['children']= list()
    # node1 = Node('B1',2,False,'B')
    # node2 = Node('B2',3,False,'B')
    # node3 = Node('B1C',5,True,'B1')
    # node_list =[node1,node2,node3]
    # add_children_node(root_node,node_list)
    # print root_node
    """
    该函数的使用方法：执行完save_tree_data后，对应树状结构的数据会以js文件的方式保存在const.JSON_PATH文件中，
    要查看生成的树状图，请打开innojoy_calculate目录下的test.html（右键打开方式-》以浏览器打开）
    """
    base_data_list = read_xls_data.read_data()
    save_tree_data(base_data_list)