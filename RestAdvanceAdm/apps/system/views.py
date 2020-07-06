import json

from django.contrib.auth import get_user_model
from django.db.models import QuerySet
from django.forms import model_to_dict
from django.shortcuts import render
from .models import *
from .serializers import *
from .utils.basemodelviewsets import *

User = get_user_model()

# Create your views here.



class ButtonTypeViewSets(CustomBaseModelViewSet):
    serializer_class = ButtonTypeSerializer
    queryset = ButtonType.objects.all()

class PermissionViewSets(CustomBaseModelViewSet):

    serializer_class = PermissionSerializer
    queryset = Permission.objects.all()


class RoleViewSets(CustomBaseModelViewSet):
    serializer_class = RoleSerializer
    queryset = Role.objects.all()

class UserViewSets(CustomBaseModelViewSet):
    serializer_class = UserSerializer
    queryset = UserProfile.objects.all()


class UserPermissionViewSets(CustomBaseModelViewSet):

    serializer_class = serializers.Serializer
    def retrieve(self, request, *args, **kwargs):

        pk = kwargs['pk']
        roles = UserProfile.objects.values('roles').filter(id = pk)

        permissions = Role.objects.values('permission').filter(id__in = [role['roles'] for role in roles])
        res = Permission.objects.values('id','name','code','parent_id','type').filter(id__in=[permission['permission'] for permission in permissions]).distinct()
        # res = PermissionJsonSerializer(res,many=True).data
        # res = [model_to_dict(x) for x in res]





        mp1 = dict()
        data1 = Permission.objects.values('id', 'name', 'code', 'parent_id', 'type').all()
        res1 = self.build_tree_all(data=data1, p_id=None,mp=mp1)

        res = self.build_tree(data=res, p_id=None, mp=mp1)

        return JsonResponse(data=res,msg="success",code=200,status=status.HTTP_200_OK)

    def build_tree_all(self,data, p_id,mp):
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
                child = self.build_tree_all(data, row['id'],mp)
                row['child'] = []
                if child:
                    if row['type'] == 2:
                        #在这里进行处理
                        child = [x['code'] for x in child]
                        mp[row['id']] = child
                    row['child'] += child
                tree.append(row)
        return tree

    def build_tree(self,data, p_id,mp):
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
                child = self.build_tree(data, row['id'],mp)
                row['child'] = []
                row['actionsOptions'] = []
                row['checkAll'] = False
                if child:
                    if row['type'] == 2:
                        #在这里进行处理
                        child = [x['code'] for x in child]
                    row['child'] += child
                    if row['id'] in mp.keys():
                        row['actionsOptions'] += mp[row['id']]
                        row['checkAll'] = True if len(row['actionsOptions']) == len(row['child']) else False
                tree.append(row)
        return tree
