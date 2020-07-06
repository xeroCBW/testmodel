### django问题总结
1. dajngo目前还不支持多个结果集一个spi返回,如果要使用;可以使用插件;但是插件貌似停止跟新`django-rest-mutiple-models`
2. 如果想在对象中嵌套对象,但是不生成数据库的表,可以`managed= False`
3. 这里使用了自定义的response 这个response 继承于 rest Response