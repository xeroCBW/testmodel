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
