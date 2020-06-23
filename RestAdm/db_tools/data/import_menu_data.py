# db_tools/data/import_category_data.py


# 独立使用django的model
import json
import sys
import os
#  获取当前文件的路径，以及路径的父级文件夹名
pwd = os.path.dirname(os.path.realpath(__file__))
# 将项目目录加入setting
sys.path.append(pwd + "../")
# manage.py中
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "RestAdm.settings")

import django
django.setup()

# 这行代码必须在初始化django之后
from system.models import *


def load():
    with open('menu.json','r') as f:
        data = json.load(f)
        return data





# 一级分类
for lev1_cat in load()['results']:

    lev1_intance = Menu()
    lev1_intance.is_top = lev1_cat["is_top"]
    lev1_intance.menu_type = lev1_cat["menu_type"]
    lev1_intance.name = lev1_cat["name"]
    lev1_intance.parent = lev1_cat["parent"]
    lev1_intance.url = lev1_cat["url"]
    lev1_intance.save()

    #二级分类
    for lev2_cat in lev1_cat["sub_menu"]:

        lev2_intance = Menu()
        lev2_intance.is_top = lev2_cat["is_top"]
        lev2_intance.menu_type = lev2_cat["menu_type"]
        lev2_intance.name = lev2_cat["name"]
        lev2_intance.parent = lev2_cat["parent"]
        lev2_intance.url = lev2_cat["url"]
        lev2_intance.save()

        #三级分类
        for lev3_cat in lev2_cat["sub_menu"]:
            lev3_intance = Menu()
            lev3_intance.is_top = lev3_cat["is_top"]
            lev3_intance.menu_type = lev3_cat["menu_type"]
            lev3_intance.name = lev3_cat["name"]
            lev3_intance.parent = lev3_cat["parent"]
            lev3_intance.url = lev3_cat["url"]
            lev3_intance.save()

