
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
