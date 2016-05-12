# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-11 20:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20160508_0236'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts',
            name='slogan',
            field=models.CharField(blank=True, max_length=700, verbose_name='Девиз'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='adress',
            field=models.CharField(max_length=154, verbose_name='адрес'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='map_adress',
            field=models.CharField(max_length=140, verbose_name='адрес для карты'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='phone',
            field=models.CharField(max_length=21, verbose_name='телефон'),
        ),
    ]