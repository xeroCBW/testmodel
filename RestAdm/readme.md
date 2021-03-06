
### 数据的导入导出
1. python manage.py dumpdata > db.json.
2. Change the database settings to new database such as of MySQL / PostgreSQL.
3. python manage.py migrate.
4. python manage.py shell. Enter the following in the shell. from django.contrib.contenttypes.models import ContentType. ContentType.objects.all().delete()
5. python manage.py loaddata db.json.

### 数据导出

```
python manage.py dumpdata > db.json
```

### 启动项目
```
nohup python manage.py runserver 0.0.0.0:80 &
```

### 导出requirement

```
pip freeze > requirements.txt
```

### 没有的字段序列化

1. 可以通过elated_name对字段进行添加
2. OneToOneField 继承于 foreignKey
3. field 都有source这个字段
4. 貌似hyperLinkRelate不能显示图片
5. 可以设置通用tag,具体详情见[通用关系](https://github.com/fangweiren/Django-REST-framework-documentation/blob/master/API-Guide/Serializer-relations.md)
6. 设置时间可以设置成readonly = true 这样就不会要求用户算时间了
7. lookup_field = 'goods_id' /user/1/ 这个是url 数字中搜索的ID
8. 可以再model 和 serializer 进行数据的校验
9. 设置成外键的时候,一定要设置成自己
10. 设置金钱的时候用decaimal digit 是总数 place 是小数
11. 超级用户可以查看所有,自己只能查看自己这个还没有思路
12. 添加过滤器之后的查询链接为:http://localhost:8000/system/good/?is_new=true&is_hot=true
要用到的类有:控件 + 自定义类
    
    ```python
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_class = GoodFilter
    ```

13. 自定义实现购物车逻辑,同时失灵hyperLinkRelate 实现快速定位购物车(一个用户是多个购物车编号的,通过用户来聚合的)
14. 为什么要保存当时的订单号,因为用户可能在下订单后修改,所以保存下单时刻的订单
14. 生成订单号,年月日时分秒+两位数随机数
15. 设置retrieve 本质是pageView 每次进去后,就会将商品的浏览数量加一
16. 通过signal来导入信号量
17 .商品的库存数量,是基于购物车;购物车加入商品就减去;购物车新增,商品也减去;购物车清空商品数量加
18. JsonResponse 继承于 HttpResponse
19. orderdict()只能放一个元素,注意不能放多个,多个用数组括起来[]
20. hasattr(response,'accepted_media_type')判断是否有某个属性
21. pip 和python 环境不一致,导致包不同[移除原先链接,增加新的链接](https://stackoverflow.com/questions/43743509/how-to-make-python3-command-run-python-3-6-instead-of-3-5)
22. 登录登出要关闭csrf这个验证,否者会遇到很多问题
23. log不能使用request.POST方法
24. group 和 permission 删除之后速度就快了
25. 跨域遇到的问题[github链接](https://github.com/adamchainz/django-cors-headers#configuration)
    ```python
    INSTALLED_APPS = [
        ...
        'corsheaders',
        ...
    ]
    MIDDLEWARE = [
        ...
        'corsheaders.middleware.CorsMiddleware',
        'django.middleware.common.CommonMiddleware',
        ...
    ]
    CORS_ORIGIN_WHITELIST = [
        "https://example.com",
        "https://sub.example.com",
        "http://localhost:8080",
        "http://127.0.0.1:9000"
    ]
    CORS_ALLOW_METHODS = [
        'DELETE',
        'GET',
        'OPTIONS',
        'PATCH',
        'POST',
        'PUT',
    ]
    from corsheaders.defaults import default_headers
    
    CORS_ALLOW_HEADERS = list(default_headers) + [
        'my-custom-header',
    ]
    CORS_ALLOW_CREDENTIALS = True
    CORS_ORIGIN_ALLOW_ALL = True
    ```
26. 使用slug 和单独使用to_represent 都是很耗性能
27. 使用serializer 会很耗性能
28. 数据查询`page_role__id__in`
29. 不知道查询为什么有时候去不了重复
30. 不确定自己写的查询语句之前,现在shell 中查询,python manage.py shell/from system.models import *
31. debug-toolbar 对docs 不起作用
32. @property 默认生成 getter方法 
    ```python
    class Student(object):
    
        @property
        def score(self):
            return self._score
    
        @score.setter
        def score(self, value):
            if not isinstance(value, int):
                raise ValueError('score must be an integer!')
            if value < 0 or value > 100:
                raise ValueError('score must between 0 ~ 100!')
            self._score = value

    ```
    结果如下:
    ```
    >>> s = Student()
    >>> s.score = 60 # OK，实际转化为s.set_score(60)
    >>> s.score # OK，实际转化为s.get_score()
    60
    >>> s.score = 9999
    Traceback (most recent call last):
      ...
    ValueError: score must between 0 ~ 100!
    ```
32. 修改数据库null = True blank = True ,要同步python文件,否则还会报错
### 查询优化
1. 一对多方面,使用related_name 可以查询出所有的多:page = Page.objects.all() page[0].button_page.all().value('id','name')
2. 多对多,直接使用属性进行查询 role = Role.objects.all() role[0].button_list.all().value('id',''name','button_page')
    ```
    roles = Role.objects.all()
    buttons = roles[0].button_list.values('id','name','url','button_role').all
    
    ```
    对应的sql
    ```
    SELECT `system_button`.`id`, `system_button`.`name`, `system_role_button_list`.`role_id` FROM `system_button` INNER JOIN `system_role_button_list` ON (`system_button`.`id` = `system_role_button_list`.`button_id`) WHERE `system_role_button_list`.`role_id` = 1 ORDER BY `system_button`.`id` DESC  LIMIT 21
    ```
    如果不使用关联,会直接查询page页面
    ```
    roles = Role.objects.all()
    roles[0].button_list.values('id','name','url')
    
    SELECT `system_role`.`id`, `system_role`.`desc`, `system_role`.`state`, `system_role`.`create_time`, `system_role`.`update_time`, `system_role`.`name`, `system_role`.`code` FROM `system_role` ORDER BY `system_role`.`id` DESC  LIMIT 1
    
    ```
        
    
3. 多对多查询要首先查出数据来,再prefetch_selected进行一对多查询;如果反向查询加filter(related_name)会导致多加一层inner join;例如
    ```
    pages_list = Button.objects.values('id','button_role').filter(button_role__in=roles).distinct()
    ```
    sql为:
    ```
    SELECT
        `system_button`.`id`,
        `system_button`.`url`,
        `system_button`.`name`,
        `system_role_button_list`.`role_id` 
    FROM
        `system_button`
        LEFT OUTER JOIN `system_role_button_list` ON ( `system_button`.`id` = `system_role_button_list`.`button_id` ) 
    ORDER BY
        `system_button`.`id` DESC 
    LIMIT 21
	
    ```

4. 多对多查询实例
    ```
    areas = Area.objects.filter(id__in=[1, 2, 3]).order_by('name').prefetch_related('role_set')
    
    for area in areas:
        roles = area.role_set.all()
        for role in roles:
            print area.name, roles.name
    ```
    
5. 多对多查询,这个可能会造成两条查询,直接使用page来查询会快一些
    ```
    #不能排序--1条记录一条sql
    pages = Page3Serializer(many=True,read_only=True,source='page_list')
    #可以排序
    pages = serializers.SerializerMethodField()
    
    def get_pages(self,obj):
    
        # print('=================')
        # 这个是通过manytomany 进行查询---2条sql
        # pages = Role.get_page_list_by_id(obj.id)
        
        # 这个是通过中间关联 的主键查询的----一条sql
        pages = Page.objects.values('id','name','desc','url','order','state').filter(page_role=obj.id).order_by('order')
    
        return Page3Serializer(pages,many=True, read_only=True).data
    ```

### 开启跨域

1. pip install django-cors-headers==2.2.0
2. installed_apps 装入app

INSTALLED_APPS = [
    'corsheaders',
]

3. 加入middleware 放入第一个
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
]

4. CORS_ORIGIN_ALLOW_ALL = True
5. 允许携带cookie CORS_ALLOW_CREDENTIALS = True


[跨域链接](https://segmentfault.com/a/1190000018025987)

### 关于外网访问

#### 局域网内访问

1. 在终端中运行 $ python3 manage.py runserver 0.0.0.0:8000 开启 django dev server 。注：因为 $ python3 manage.py runserver 默认运行的是 $ python3 manage.py runserver 127.0.0.1:8000 （默认是 8000 端口）即运行本地 localhost 服务
2. 在 settings.py 中添加服务器（本机）局域网 IP 地址实现局域网内「IP+端口号」访问
```
# ALLOWED_HOSTS = []
ALLOWED_HOSTS = [ '192.168.x.xxx' ]
```
3. 此时局域网内访问 192.168.x.xxx:8000/admin 即可访问 Django 的 admin 页面

[网络访问链接](https://github.com/FatliTalk/blog/issues/76)

### 数据输入/输出:
#### 文件下载
1. 使用插件drf-csv
2. 使用drf-pandas,设置好类
3. 重写render类,否者pagination分页结果不一致会报错
#### 文件上传
1. 当使用parser_classes = (MultiPartParser,)这种方式上传附件时，客户端请求请求头不能有Content-Type，否则会报错


### pip使用
1. pip install --upgrade xxx
2. pip install xxx==yyy
3. pip freeze > requirements.txt


### igraph画图
1. 一定要安装这个`pip install pycairo` 否则会报错