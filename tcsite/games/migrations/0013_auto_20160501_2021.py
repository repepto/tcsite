# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-01 17:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0012_auto_20160501_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topimage',
            name='image',
            field=models.ImageField(upload_to='games/main_top_image', verbose_name='Top image'),
        ),
    ]