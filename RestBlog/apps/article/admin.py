from django.contrib import admin
from django.contrib.admin.models import LogEntry
# Register your models here.
from .models import Category,Tag,Post,Link,SliderBar

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name','is_nav','status','create_time','update_time')
    fields = ('name','is_nav','status',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id','name','status','create_time','update_time')
    fields = ('name','status')

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


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('id','name','href','status','create_time','update_time')
    fields = ('name','href','status')


@admin.register(SliderBar)
class SliderBarAdmin(admin.ModelAdmin):
    list_display = ('name','content','type','status','create_time','update_time')
    fields = ('name','content','type')

@admin.register(LogEntry)
class LoginEntryAdmin(admin.ModelAdmin):
    list_display = ('id','object_id','object_repr','action_flag','user','change_message',)
