### 数据的导入导出
1. python manage.py dumpdata > db.json.
2. Change the database settings to new database such as of MySQL / PostgreSQL.
3. python manage.py migrate.
4. python manage.py shell. Enter the following in the shell. from django.contrib.contenttypes.models import ContentType. ContentType.objects.all().delete()
5. python manage.py loaddata db.json.

### 数据导出

```
python manage.py dumpdata > dp.json
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