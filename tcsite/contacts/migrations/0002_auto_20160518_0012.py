# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-17 21:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='map_adress',
            field=models.CharField(default='Киев. Украина', max_length=140, verbose_name='адрес для карты'),
        ),
    ]
