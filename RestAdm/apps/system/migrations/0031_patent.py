# Generated by Django 2.2.5 on 2020-08-05 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0030_page_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField(blank=True, max_length=1000, null=True)),
                ('state', models.BooleanField(default=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='创建时间', verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, help_text='修改时间', verbose_name='修改时间')),
                ('document_no', models.CharField(blank=True, help_text='文献号', max_length=100, null=True, verbose_name='文献号')),
                ('apply_no', models.CharField(blank=True, help_text='申请号', max_length=100, null=True, verbose_name='申请号')),
                ('apply_time', models.CharField(blank=True, help_text='申请时间', max_length=100, null=True, verbose_name='申请时间')),
                ('public_no', models.CharField(blank=True, help_text='公开号', max_length=100, null=True, verbose_name='公开号')),
                ('public_time', models.CharField(blank=True, help_text='公开时间', max_length=100, null=True, verbose_name='公开时间')),
                ('name', models.CharField(blank=True, help_text='名称', max_length=100, null=True, verbose_name='名称')),
                ('apply_user', models.CharField(blank=True, help_text='申请用户', max_length=100, null=True, verbose_name='申请用户')),
                ('address', models.CharField(blank=True, help_text='申请人地址', max_length=100, null=True, verbose_name='申请人地址')),
                ('inventor', models.CharField(blank=True, help_text='发明者', max_length=100, null=True, verbose_name='发明者')),
                ('priority', models.CharField(blank=True, help_text='优先级', max_length=100, null=True, verbose_name='优先级')),
                ('category_no', models.CharField(blank=True, help_text='分类号', max_length=100, null=True, verbose_name='分类号')),
                ('main_category_no', models.CharField(blank=True, help_text='主要分类号', max_length=100, null=True, verbose_name='主要分类号')),
                ('nation_province', models.CharField(blank=True, help_text='国家省份', max_length=100, null=True, verbose_name='国家省份')),
                ('internation_publish', models.CharField(blank=True, help_text='国际发布', max_length=100, null=True, verbose_name='国际发布')),
                ('internation_publish_time', models.CharField(blank=True, help_text='国际发布时间', max_length=100, null=True, verbose_name='国际发布时间')),
                ('phrator_date', models.CharField(blank=True, help_text='同族', max_length=100, null=True, verbose_name='同族')),
                ('quote_number', models.IntegerField(default=0, help_text='被引用数量', verbose_name='被引用数量')),
                ('quote_patent', models.CharField(blank=True, help_text='引用专利', max_length=100, null=True, verbose_name='引用专利')),
                ('abstract', models.CharField(blank=True, help_text='摘要', max_length=100, null=True, verbose_name='摘要')),
                ('abstract_pic', models.CharField(blank=True, help_text='摘要图片', max_length=100, null=True, verbose_name='摘要图片')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]