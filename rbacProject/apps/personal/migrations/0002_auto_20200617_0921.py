# Generated by Django 2.1.5 on 2020-06-17 09:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('personal', '0001_initial'),
        ('adm', '0002_auto_20200617_0921'),
    ]

    operations = [
        migrations.AddField(
            model_name='workorderrecord',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='记录人'),
        ),
        migrations.AddField(
            model_name='workorderrecord',
            name='work_order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.WorkOrder', verbose_name='工单信息'),
        ),
        migrations.AddField(
            model_name='workorder',
            name='approver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='approver', to=settings.AUTH_USER_MODEL, verbose_name='审批人'),
        ),
        migrations.AddField(
            model_name='workorder',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adm.Customer', verbose_name='客户信息'),
        ),
        migrations.AddField(
            model_name='workorder',
            name='proposer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='proposer', to=settings.AUTH_USER_MODEL, verbose_name='申请人'),
        ),
        migrations.AddField(
            model_name='workorder',
            name='receiver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to=settings.AUTH_USER_MODEL, verbose_name='接单人'),
        ),
    ]
