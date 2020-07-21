### django问题总结
1. dajngo目前还不支持多个结果集一个spi返回,如果要使用;可以使用插件;但是插件貌似停止跟新`django-rest-mutiple-models`
2. 如果想在对象中嵌套对象,但是不生成数据库的表,可以`managed= False`
3. 这里使用了自定义的response 这个response 继承于 rest Response
4. allow_null 序列化可以设置成空
5. 对数据进行校验
    ```
    
    def validate(self, data):
            """
            Check that the start is before the stop.
            """
            if data['start'] > data['finish']:
                raise serializers.ValidationError("finish must occur after start")
            return data
    
    ```
6 .对数据进行递归查询,但是不建议[stackOverFlow解答](https://stackoverflow.com/questions/13376894/django-rest-framework-nested-self-referential-objects)

    ```
        def get_related_field(self, model_field):
            return PermissionDetailSerializer()
    
    
    class RecursiveField(serializers.Serializer):
        def to_representation(self, value):
            serializer = self.parent.parent.__class__(value, context=self.context)
            return serializer.data
    
    ```
7. 若要从多个结果集,返回,直接建议使用json来拼接,这样是目前最快的方法
8. 使用递归会访问数据库多次
9. 数据request.data 在 create /update 是 immutable不可以更改的[修改request的请求数据](https://stackoverflow.com/questions/44717442/this-querydict-instance-is-immutable/51196932)
    
    ```
        _mutable = data._mutable
        
        # set to mutable
        data._mutable = True
        
        # сhange the values you want
        data['param_name'] = 'new value'
        
        # set mutable flag back
        data._mutable = _mutable
    
    ```

10. 设置默认用户这个有点麻烦
    
    ```
       create_user = serializers.HiddenField(
            default=serializers.CurrentUserDefault().user.id
        )
        update_user = serializers.HiddenField(
    
            default=serializers.CurrentUserDefault().user.id
        )
    
    ```

### 类似项目参照:
1. 懒加载,用到了采取加载下一级
2. 有index这个页面
3. 权限只做了部门这一级别,根据部门去过滤数据
4. 登录之后,返回左边的菜单,只是返回菜单,没有返回按钮
    ```json
    {
        "name": "多级菜单",
        "path": "/nested",
        "hidden": false,
        "redirect": "noredirect",
        "component": "Layout",
        "alwaysShow": true,
        "meta": {
            "title": "多级菜单",
            "icon": "menu",
            "noCache": true
        },
        "children": [
            {
                "name": "二级菜单2",
                "path": "menu2",
                "hidden": false,
                "component": "nested/menu2/index",
                "meta": {
                    "title": "二级菜单2",
                    "icon": "menu",
                    "noCache": true
                }
            },
            {
                "name": "二级菜单1",
                "path": "menu1",
                "hidden": false,
                "redirect": "noredirect",
                "component": "nested/menu1/index",
                "alwaysShow": true,
                "meta": {
                    "title": "二级菜单1",
                    "icon": "menu",
                    "noCache": true
                },
                "children": [
                    {
                        "name": "三级菜单1",
                        "path": "menu1-1",
                        "hidden": false,
                        "component": "nested/menu1/menu1-1",
                        "meta": {
                            "title": "三级菜单1",
                            "icon": "menu",
                            "noCache": true
                        }
                    },
                    {
                        "name": "三级菜单2",
                        "path": "menu1-2",
                        "hidden": false,
                        "component": "nested/menu1/menu1-2",
                        "meta": {
                            "title": "三级菜单2",
                            "icon": "menu",
                            "noCache": true
                        }
                    }
                ]
            }
        ]
    }
    
    ```

5. 3个用户,返回3条记录,记录中有部门dept:[] menu:[],其中menu不进行层次划分(可以进行树状划分)[请求地址](https://api.auauz.net/api/menus/lazy?pid=1)

    ```json
    
    {
        "createBy": "admin",
        "updatedBy": "admin",
        "createTime": 1594094492000,
        "updateTime": 1594095966000,
        "id": 3,
        "menus": [
            {
                "createBy": null,
                "updatedBy": null,
                "createTime": 1545117089000,
                "updateTime": null,
                "id": 1,
                "children": null,
                "type": 0,
                "permission": null,
                "title": "系统管理",
                "menuSort": 1,
                "path": "system",
                "component": null,
                "pid": null,
                "subCount": 7,
                "cache": false,
                "hidden": false,
                "componentName": null,
                "icon": "system",
                "label": "系统管理",
                "iframe": false,
                "hasChildren": true,
                "leaf": false
            },
            {
                "createBy": null,
                "updatedBy": null,
                "createTime": 1545117284000,
                "updateTime": null,
                "id": 2,
                "children": null,
                "type": 1,
                "permission": "user:list",
                "title": "用户管理",
                "menuSort": 2,
                "path": "user",
                "component": "system/user/index",
                "pid": 1,
                "subCount": 3,
                "cache": false,
                "hidden": false,
                "componentName": "User",
                "icon": "peoples",
                "label": "用户管理",
                "iframe": false,
                "hasChildren": true,
                "leaf": false
            },
            {
                "createBy": null,
                "updatedBy": null,
                "createTime": 1573960113000,
                "updateTime": null,
                "id": 103,
                "children": null,
                "type": 2,
                "permission": "serverDeploy:add",
                "title": "服务器新增",
                "menuSort": 999,
                "path": "",
                "component": "",
                "pid": 92,
                "subCount": 0,
                "cache": false,
                "hidden": false,
                "componentName": null,
                "icon": "",
                "label": "服务器新增",
                "iframe": false,
                "hasChildren": false,
                "leaf": true
            },
            {
                "createBy": null,
                "updatedBy": null,
                "createTime": 1573960137000,
                "updateTime": null,
                "id": 104,
                "children": null,
                "type": 2,
                "permission": "serverDeploy:edit",
                "title": "服务器编辑",
                "menuSort": 999,
                "path": "",
                "component": "",
                "pid": 92,
                "subCount": 0,
                "cache": false,
                "hidden": false,
                "componentName": null,
                "icon": "",
                "label": "服务器编辑",
                "iframe": false,
                "hasChildren": false,
                "leaf": true
            },
            {
                "createBy": null,
                "updatedBy": null,
                "createTime": 1573266668000,
                "updateTime": null,
                "id": 90,
                "children": null,
                "type": 1,
                "permission": null,
                "title": "运维管理",
                "menuSort": 20,
                "path": "mnt",
                "component": "",
                "pid": null,
                "subCount": 5,
                "cache": false,
                "hidden": false,
                "componentName": "Mnt",
                "icon": "mnt",
                "label": "运维管理",
                "iframe": false,
                "hasChildren": true,
                "leaf": false
            },
            {
                "createBy": null,
                "updatedBy": null,
                "createTime": 1573960203000,
                "updateTime": null,
                "id": 106,
                "children": null,
                "type": 2,
                "permission": "app:add",
                "title": "应用新增",
                "menuSort": 999,
                "path": "",
                "component": "",
                "pid": 93,
                "subCount": 0,
                "cache": false,
                "hidden": false,
                "componentName": null,
                "icon": "",
                "label": "应用新增",
                "iframe": false,
                "hasChildren": false,
                "leaf": true
            },
            {
                "createBy": null,
                "updatedBy": null,
                "createTime": 1573960228000,
                "updateTime": null,
                "id": 107,
                "children": null,
                "type": 2,
                "permission": "app:edit",
                "title": "应用编辑",
                "menuSort": 999,
                "path": "",
                "component": "",
                "pid": 93,
                "subCount": 0,
                "cache": false,
                "hidden": false,
                "componentName": null,
                "icon": "",
                "label": "应用编辑",
                "iframe": false,
                "hasChildren": false,
                "leaf": true
            },
            {
                "createBy": null,
                "updatedBy": null,
                "createTime": 1572317986000,
                "updateTime": null,
                "id": 44,
                "children": null,
                "type": 2,
                "permission": "user:add",
                "title": "用户新增",
                "menuSort": 2,
                "path": "",
                "component": "",
                "pid": 2,
                "subCount": 0,
                "cache": false,
                "hidden": false,
                "componentName": null,
                "icon": "",
                "label": "用户新增",
                "iframe": false,
                "hasChildren": false,
                "leaf": true
            },
            {
                "createBy": null,
                "updatedBy": null,
                "createTime": 1572318008000,
                "updateTime": null,
                "id": 45,
                "children": null,
                "type": 2,
                "permission": "user:edit",
                "title": "用户编辑",
                "menuSort": 3,
                "path": "",
                "component": "",
                "pid": 2,
                "subCount": 0,
                "cache": false,
                "hidden": false,
                "componentName": null,
                "icon": "",
                "label": "用户编辑",
                "iframe": false,
                "hasChildren": false,
                "leaf": true
            },
            {
                "createBy": null,
                "updatedBy": null,
                "createTime": 1573355116000,
                "updateTime": null,
                "id": 93,
                "children": null,
                "type": 1,
                "permission": "app:list",
                "title": "应用管理",
                "menuSort": 23,
                "path": "mnt/app",
                "component": "mnt/app/index",
                "pid": 90,
                "subCount": 3,
                "cache": false,
                "hidden": false,
                "componentName": "App",
                "icon": "app",
                "label": "应用管理",
                "iframe": false,
                "hasChildren": true,
                "leaf": false
            }
        ],
        "depts": [
            {
                "createBy": null,
                "updatedBy": "admin",
                "createTime": 1553483090000,
                "updateTime": 1589111952000,
                "id": 7,
                "name": "华南分部",
                "enabled": true,
                "deptSort": 0,
                "pid": null,
                "subCount": 2,
                "label": "华南分部",
                "hasChildren": true,
                "leaf": false
            }
        ],
        "name": "test1",
        "dataScope": "自定义",
        "level": 2,
        "description": null
    }
    
    
    ```
6. 根据pid 来查子类的菜单
7. 修改角色权限传的参数太多,可以使用menus:[1,2,3]
8. 安装mq模拟启动`python manage.py celery worker --loglevel=info`
9. 初步完成flower和work搭建
```
celery -A RestAdvanceAdm worker -l info
celery -A RestAdvanceAdm flower -l info --persistent=True
```


