import json
import re

from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """权限认证"""
    message = "没有权限访问"

    def has_permission(self, request, view):


        # return  False

        next_url = request.path_info
        next_method = request.method
        print(next_url,'---',next_method)

        if next_url == "/system/global/":
            return True

        top_menu,reveal_menu,permission_url_list = self.get_menu(request)

        # 返回首页
        for x in top_menu:
            if x["url"] == next_url:
                return True


        # a = {
        #
        #     'top_menu': top_menu,
        #     'reveal_menu': reveal_menu,
        #     'permission_url_list': permission_url_list,
        # }
        # print('-----------')
        # print(json.dumps(a))

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
                tmp_url += "list"

        elif next_method == "POST":
            # 创建
            tmp_url += "create"

        elif next_method == "PUT":
            # 修改
            tmp_url += "update"

        elif next_method == "DELETE":
            # 修改
            tmp_url += "delete"

        if tmp_url in permission_url_list:
            return True

        return  False
    def get_menu(self, request):
        """
        获取用户权限菜单：这个地方真的好乱，没有更好的实现方法只能先忍受下吧
        :param request:
        :return:
        """

        if request.user.is_authenticated:

            user = request.user
            permissions_item_list = user.roles.values('permissions__id',
                                                      'permissions__title',
                                                      'permissions__url',
                                                      'permissions__icon',
                                                      'permissions__code',
                                                      'permissions__parent').distinct()

            permission_url_list = []
            permission_menu_list = []

            for item in permissions_item_list:
                # print('-----',item['permissions__url'])
                permission_url_list.append(item['permissions__url'])
                if item['permissions__id']:
                    menu = {
                        'id': item['permissions__id'],
                        'title': item['permissions__title'],
                        'url': item['permissions__url'],
                        'icon': item['permissions__icon'],
                        'code': item['permissions__code'],
                        'parent': item['permissions__parent'],
                        'status': False,
                        'sub_menu': [],

                    }
                    permission_menu_list.append(menu)

            request_url = request.path_info
            top_menu = []
            permission_menu_dict = {}
            for menu in permission_menu_list:

                url = menu['url']
                if url and re.match(url, request_url):
                    menu['status'] = True
                if menu['parent'] is None:
                    top_menu.insert(0, menu)
                permission_menu_dict[menu['id']] = menu

            menu_data = []
            for i in permission_menu_dict:
                if permission_menu_dict[i]['parent']:
                    pid = permission_menu_dict[i]['parent']
                    parent_menu = permission_menu_dict[pid]
                    parent_menu['sub_menu'].append(permission_menu_dict[i])
                else:
                    menu_data.append(permission_menu_dict[i])

            if [menu['sub_menu'] for menu in menu_data if menu['url'] in request_url]:
                reveal_menu = [menu['sub_menu'] for menu in menu_data if menu['url'] in request_url][0]
            else:
                reveal_menu = None

            return top_menu, reveal_menu, permission_url_list
        else:
            pass




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