# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-11 21:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20160511_2157'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['post_order'], 'verbose_name': 'Пост', 'verbose_name_plural': 'Посты'},
        ),
    ]