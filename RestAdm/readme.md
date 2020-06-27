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
