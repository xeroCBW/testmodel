
# coding: utf-8 -*-
import xlrd
import sys
import exceptions
import numpy as np
import innojoy_calculate.common.const as const


def read_data():
    """
    按照BASE_MAP读取原始数据,并保存为list
    :param data_path:
    :return:
    """
    if const.BASE_PATH != '':
        reload(sys)
        sys.setdefaultencoding('utf-8')
        return_list = list()
        # 打开Excel文件读取数据
        data = xlrd.open_workbook(const.BASE_PATH)
        # 获取第一个工作表
        table = data.sheet_by_index(const.BASE_MAP['SHEET_NBR'])
        # 行数
        nrows = table.nrows
        #从第一行开始读取数据
        for row in range(1, nrows):
            row_dict = dict()
            # 申请日
            row_dict[const.APPLY_DATE] = table.cell(row, const.BASE_MAP[const.APPLY_DATE]).value.encode('utf-8')
            # 申请人
            row_dict[const.APPLICANT] = table.cell(row, const.BASE_MAP[const.APPLICANT]).value.encode('utf-8')
            # 发明人
            row_dict[const.INVENTOR] = table.cell(row, const.BASE_MAP[const.INVENTOR]).value.encode('utf-8')
            # 分类号
            row_dict[const.CLASS_NBR] = table.cell(row, const.BASE_MAP[const.CLASS_NBR]).value.encode('utf-8')
            return_list.append(row_dict)
        return return_list
    else:
        raise exceptions('没有配置文件地址！')

