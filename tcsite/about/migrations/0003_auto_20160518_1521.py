# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-18 12:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_aboutmetatags'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'ordering': ['the_order'], 'verbose_name': 'О салоне', 'verbose_name_plural': '1: О салоне'},
        ),
        migrations.AlterModelOptions(
            name='aboutmetatags',
            options={'verbose_name': 'МетаТэги', 'verbose_name_plural': '2: МетаТэги'},
        ),
    ]