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
    with open('data/structure.json','r') as f:
        data = json.load(f)
        return data


# 一级分类
for lev1_cat in load()['results']:

    lev1_intance = Structure()
    lev1_intance.type = lev1_cat["type"]
    lev1_intance.name = lev1_cat["name"]
    lev1_intance.parent = None
    print(lev1_intance.name)
    lev1_intance.save()

    #二级分类
    for lev2_cat in lev1_cat["sub_structure"]:

        lev2_intance = Structure()
        lev2_intance.type = lev2_cat["type"]
        lev2_intance.name = lev2_cat["name"]
        lev2_intance.parent = lev1_intance

        print(lev2_intance.name)
        lev2_intance.save()

