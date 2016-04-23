# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-22 20:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='game',
            options={'ordering': ['the_order'], 'verbose_name': 'Games', 'verbose_name_plural': 'Game objects'},
        ),
        migrations.AddField(
            model_name='game',
            name='preview',
            field=models.ImageField(default='aaa', upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='game',
            name='bottom_description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='game',
            name='middle_description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='game',
            name='top_description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='game',
            name='top_description_italic',
            field=models.TextField(default=''),
        ),
    ]
