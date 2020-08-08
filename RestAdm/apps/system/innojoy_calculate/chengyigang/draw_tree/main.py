# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = xiongliff
__mtime__ = '2019/7/20'
"""
from utils import read_xls_data
from chengyigang.draw_tree import tree_node
import  numpy as np
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
    #base_data_list = read_xls_data.read_data()
    #tree_node.save_tree_data(base_data_list)
    a = [[1,2]]
    b=[[2,3],[2,4]]
    a.extend(b)
    print(a)
 
    a=dict()
    if a.values():
        print('ss')
    print(str(None))
    a= ''
    for i in range(13):
        a+='%s'
    print(a)
    print(int(20))