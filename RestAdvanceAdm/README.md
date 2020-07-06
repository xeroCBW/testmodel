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