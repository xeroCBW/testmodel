import json
import re

from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """权限认证"""
    message = "没有权限访问"

    def has_permission(self, request, view):

        if not request.user.is_authenticated:return False

        user = request.user

        next_url = request.path_info
        next_method = request.method
        print(next_url, '---', next_method)

        # 放行查询
        if next_url.startswith('/system/user-permission'):return True

        permissions_item_list = user.role_list.values('menu_list__url',).distinct()
        permissions_item_list = list(permissions_item_list)
        permissions_item_list = [item["menu_list__url"] for item in permissions_item_list]

        print(permissions_item_list)

        tmp_url = next_url
        if next_method == "GET":
            # 获取列表或者单个数据
            matchObj = re.match(r'.*/\d+/', next_url)
            # 带有数字
            if matchObj:
                l = tmp_url.split('/')
                l.pop()
                l.pop()
                tmp_url = '/'.join(l)
                tmp_url += "/detail"
            else:
                pass
                # tmp_url += "list"

        elif next_method == "POST":
            # 创建
            tmp_url += "create"

        elif next_method == "PUT":
            # 修改
            tmp_url += "update"

        elif next_method == "DELETE":
            # 修改
            tmp_url += "delete"

        # 删除最后一个和第一个
        tmp_url = tmp_url[1:-1]
        print(tmp_url)

        if tmp_url in permissions_item_list:
            return True

        return False

class UserTypePermission(permissions.BasePermission):
    """权限认证"""
    message = "只有管理员才能访问"

    def has_permission(self, request, view):
        user = request.user
        try:
            from system.models import UserProfile
            user_type = UserProfile.objects.filter(username=user).first().user_type
        except AttributeError:
            return False
        if user_type == 1:
            return True
        else:
            return False