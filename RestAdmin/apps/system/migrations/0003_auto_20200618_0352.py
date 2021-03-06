# Generated by Django 2.0.2 on 2020-06-18 03:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0002_auto_20200617_0840'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='menu_type',
            field=models.IntegerField(blank=True, choices=[(1, '一级类目'), (2, '二级类目'), (3, '三级类目')], help_text='类目级别', null=True, verbose_name='类目级别'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_menu', to='system.Menu', verbose_name='父菜单'),
        ),
    ]
