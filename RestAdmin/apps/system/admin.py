from django.contrib import admin
from .models import *
# 修改title和header
admin.site.site_title = '我的音乐后台管理系统'
admin.site.site_header = '我的音乐'

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    # 设置模型字段，用于Admin后台数据的表头设置
    list_display = ['id','title','parent','is_top','icon','code','url']
    # 设置可搜索的字段并在Admin后台数据生成搜索框，如有外键应使用双下划线连接两个模型的字段
    search_fields = ['id','title',]
    # 设置排序方式
    ordering = ['id']


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    # 设置模型字段，用于Admin后台数据的表头设置
    list_display = ['id','name','birthday','gender','mobile','email','image','department','post','superior','joined_date']
    # 设置可搜索的字段并在Admin后台数据生成搜索框，如有外键应使用双下划线连接两个模型的字段
    search_fields = ['id','name',]
    # 设置排序方式
    ordering = ['id']


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    # 设置模型字段，用于Admin后台数据的表头设置
    list_display = ['id','title']
    # 设置可搜索的字段并在Admin后台数据生成搜索框，如有外键应使用双下划线连接两个模型的字段
    search_fields = ['id','title',]
    # 设置排序方式
    ordering = ['id']



