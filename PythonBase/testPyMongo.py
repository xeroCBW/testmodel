import json
import re
from collections import deque
from typing import List# 这个只是用来声明的
# from pymongo import MongoClient


# # 注意端口不要设置错误27017 ,可以使用
# client = MongoClient(host='127.0.0.1',port=27017)
#
# collection = client['test']['mycoll2']
#
# list = collection.find()
# for item in list:
#     print(item)

# /system/basic/user/1/
# next_url = "/system/basic/user/"
# next_url = "/system/basic/user/090909090/get"
# next_url = "/system/basic/menu/?page=3"
# matchObj = re.match(r'.*/\d+/',next_url)
#
# # matchObj = re.match("/system/basic/user/090909090/",next_url)
# print(matchObj.group())


# res = "/system/user/1/"
#
# l = res.split('/')
# l.pop()
# l.pop()
# res = '/'.join(l)
#
# print(res)
from datetime import datetime


class Menu:
    def __init__(self, id, title, parent_id,):
        self._id = id
        self._title = title
        self._parent_id = parent_id
        # self._url = url
        # self._app_id = app_id
        # self._icon = icon
        # self._sortby = sort_by
        # self._create_time = create_time
        # self._update_time = update_time
        # self._subMenus = subMenus

    @property
    def id(self):
        return self._id
    @property
    def title(self):
        return self._title
    @property
    def parent_id(self):
        return self._parent_id
    # @property
    # def url(self):
    #     return self._url
    # @property
    # def app_id(self):
    #     return self._app_id
    # @property
    # def icon(self):
    #     return self._icon
    # @property
    # def sortby(self):
    #     return self._sortby
    # @property
    # def subMenus(self):
    #     return self._subMenus




def build_tree(data, p_id, level=0):
    """
    生成树菜单
    :param data:    数据
    :param p_id:    上级分类
    :param level:   当前级别
    :return:
    """
    tree = []
    for row in data:
        if row['parent_id'] == p_id:
            row['level'] = level
            child = build_tree(data, row['id'], level+1)
            row['child'] = []
            if child:
                row['child'] += child
            tree.append(row)

    return tree

data = []

menu1 = {'id':1,'parent_id':None,'title':'系统'}
menu2 = {'id':2,'parent_id':1,'title':'角色列表'}
menu3 = {'id':3,'parent_id':2,'title':'角色详情'}
menu4 = {'id':4,'parent_id':2,'title':'角色新增'}
menu5 = {'id':5,'parent_id':2,'title':'角色修改'}
menu6 = {'id':6,'parent_id':2,'title':'角色删除'}


data.append(menu1)
data.append(menu2)
data.append(menu3)
data.append(menu4)
data.append(menu5)
data.append(menu6)


ans = build_tree(data=data,p_id=None,level=0)

# print(json.dumps(ans))

# 对时间进行序列化

now = datetime.now()

# print(now)



# a = [1,2,3,4,5]
#
# for x in a:
#     print(x)
#     del  x
#
# print(a)



# a = '111222-'
# # 表示,从0开始,然后到倒数第二个
# print(a[:-1])



# print(1<<31)
# print(2**31)


# print('HHH'.lower())


# print('Anini'.istitle())

# print(max(1,2))


dic = {
    'N':(0,1),
    'S':(0,-1),
    'E':(1,0),
    'W':(-1,0),
}

# for k,v in dic.items():
#     print(v[0],v[1])


# for index ,v in enumerate(dic.items()):
#     print(index,v)

# 0 ('N', (0, 1))
# 1 ('S', (0, -1))
# 2 ('E', (1, 0))
# 3 ('W', (-1, 0))

# a = [1,2,3,4,5]
# for index,v in enumerate(a):
#     print(index,v)



# a = {
#     'code':200,
#     'data':'哈哈哈',
#     'msg':'success',
# }
#
# print(json.dumps(a,ensure_ascii=False,indent=4))


# print(len('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImNidyIsImV4cCI6MTU5Mzc2Mzg1MywiZW1haWwiOiI4NjE3NTQxODZAcXEuY29tIiwib3JpZ19pYXQiOjE1OTM2Nzc0NTN9.KChKLRXpnX2XLiWXFMQR35dRRciaA5HzSem55AxZWG4'))

# a = "Let's take LeetCode contest"
#
# b = a.split()
# for x in b:
#     y = reversed(x)
#     print(str(y))
#
# for x in b:
#     print(x)

# a = 'Hiii'
# print(a.lower())


class Solution:


    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while (i <= j):
            if not (s[i].isdigit() or s[i].isalpha()):
                i += 1
                continue

            if not (s[j].isdigit() or s[j].isalpha()):
                j -= 1
                continue

            if s[i].lower() == s[j].lower():
                i += 1
                j -= 1
                continue
            else:
                print(i,j)
                print(s[i],s[j])
                return False
        return True

# if __name__ == '__main__':
#     s = 'A man, a plan, a canal: Panama'
#     m = Solution()
#     print(m.isPalindrome(s))
#
#
# a = [1,2,3,4,5]
# print(a)
# a.reverse()
# print(a)




# mp = dict()
#
# mp['1'] = [1,2,3]
#
# print(mp)


# a = [1,2,3]
# b = [1,2,3]
# 
# if set(a) >= set(b):
#     print('true')
# else:
#     print('false')
#


# def preoder(arr):
#    for x in arr:
#        print(x)
#
# preoder([1,2,3])



# 这个是遍历,但是不会改变原来的
# a = [1,2,3]
# print(a)
# print(a[::-1])
# print(a)
# 
# 
# 
# q = deque()


# def test():
#     print('-------')
#
# test()


# print(__name__)
# if __name__ == '__main__':
#     print('hhhhhhhh')



class Brand:
    def __init__(self,name):
        self.name = name

    def __getitem__(self, item):
        print('__getitem__')
        return self.__dict__.get(item)



    def __setitem__(self, key, value):
        print('__setitem__')
        self.__dict__[key] = value

    def __delitem__(self, key):
        print('__delitem__')
        self.__dict__.pop(key)
    def __delattr__(self, item):

        print('__delattr__')
        self.__dict__.pop(item)

    def say(self):
        print('hello world...')




b = Brand('cbw')
print(b.name)
# 通过字典方式来获取对象

print(b['name'])

# del b.name
# del b['name']

