# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-16 13:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_topvideo_bg_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topvideo',
            name='bg_image',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Фон 1600х1060 (пока видео не загрузилось)'),
        ),
    ]