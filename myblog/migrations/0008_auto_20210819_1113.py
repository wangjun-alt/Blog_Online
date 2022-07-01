# Generated by Django 3.2.6 on 2021-08-19 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0007_alter_post_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_md',
            field=models.BooleanField(default=False, verbose_name='markdown语法'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(help_text='正文必须为MarkDown格式', verbose_name='正文'),
        ),
    ]