# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-21 17:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0006_auto_20160421_1858'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarouselObj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('toptitle', models.CharField(default='game design company', max_length=49)),
                ('middletitle', models.CharField(default='tabletcrushers', max_length=49)),
                ('bottomtitle', models.CharField(default='have fun, folks', max_length=49)),
                ('buttontitle', models.CharField(default='', max_length=49)),
                ('the_order', models.PositiveIntegerField(db_index=True, default=0, editable=False)),
            ],
            options={
                'verbose_name': 'CarouselObj',
                'ordering': ['the_order'],
                'verbose_name_plural': 'CarouselObj',
            },
        ),
        migrations.DeleteModel(
            name='Carousel',
        ),
    ]