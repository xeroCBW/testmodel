# Generated by Django 2.0.2 on 2020-07-10 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20200710_1341'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='link',
            options={'ordering': ['-id']},
        ),
        migrations.AddField(
            model_name='post',
            name='pv',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='post',
            name='uv',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='link',
            name='weight',
            field=models.IntegerField(default=1),
        ),
    ]
