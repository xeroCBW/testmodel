### 数据库设置
1. 设置成抽象 abstract = True
2. 设置不生成实体 managed = False
3. 对于多对多展示 ,要重写方法
    ```
    @admin.register(Post)
    class PostAdmin(admin.ModelAdmin):
        list_display = ('id','title','desc','content','category','tags','status','create_time','update_time')
        fields = ('title','desc','content','category','tag','status')
    
        def tags(self,obj):
            '''
            :param obj: 当前对象
            :return:返回所有tag展示的数据
            '''
            return "/".join([p.name for p in obj.tag.all()])
    
    ```
4. 设置显示操作日志,urllink可能会显示不出数据
    ```
    @admin.register(LogEntry)
    class LoginEntryAdmin(admin.ModelAdmin):
        list_display = ('id','object_id','object_repr','action_flag','user','change_message',)
    ```
5. url和path对比[链接](https://consideratecode.com/2018/05/02/django-2-0-url-to-path-cheatsheet/)

    ```
    
    url(r'^posts/(?P<post_id>[0-9]+)/$', post_detail_view)
    path('posts/<int:post_id>/', post_detail_view)
    
    ```
6. dict.update() 可以将另外一个dict 中的数据合并过来
7. 一定要把mixin放在前面,否者会报错
8. render_to_string() 将html代码保存,留给以后渲染用 

