# Generated by Django 2.1.5 on 2020-06-17 09:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('adm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='belongs_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='责任人'),
        ),
        migrations.AddField(
            model_name='serviceinfo',
            name='writer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='记录人'),
        ),
        migrations.AddField(
            model_name='equipment',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adm.Customer', verbose_name='客户信息'),
        ),
        migrations.AddField(
            model_name='equipment',
            name='equipment_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adm.EquipmentType', verbose_name='设备类型'),
        ),
        migrations.AddField(
            model_name='equipment',
            name='service_info',
            field=models.ManyToManyField(blank=True, to='adm.ServiceInfo', verbose_name='服务记录'),
        ),
        migrations.AddField(
            model_name='equipment',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adm.Supplier', verbose_name='分销商'),
        ),
        migrations.AddField(
            model_name='customer',
            name='belongs_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='责任人'),
        ),
        migrations.AddField(
            model_name='assetlog',
            name='asset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adm.Asset', verbose_name='资产'),
        ),
        migrations.AddField(
            model_name='assetfile',
            name='asset',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adm.Asset', verbose_name='资产'),
        ),
        migrations.AddField(
            model_name='asset',
            name='assetType',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adm.AssetType', verbose_name='资产类型'),
        ),
        migrations.AddField(
            model_name='asset',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='使用人'),
        ),
    ]
