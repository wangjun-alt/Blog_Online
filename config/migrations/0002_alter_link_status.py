# Generated by Django 3.2.6 on 2021-08-11 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='status',
            field=models.PositiveIntegerField(choices=[(1, '正常'), (1, '删除')], default=1, verbose_name='状态'),
        ),
    ]
