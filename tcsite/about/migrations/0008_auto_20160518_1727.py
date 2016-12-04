# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-18 14:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0007_auto_20160518_1643'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='promo_block',
        ),
        migrations.AddField(
            model_name='about',
            name='promo_bottom',
            field=models.CharField(blank=True, max_length=420, verbose_name='Нижняя надпись (блок с фоном под услугами)'),
        ),
        migrations.AddField(
            model_name='about',
            name='promo_buttton',
            field=models.CharField(blank=True, max_length=420, verbose_name='Надпись на кнопке (блок с фоном под услугами)'),
        ),
        migrations.AddField(
            model_name='about',
            name='promo_href',
            field=models.CharField(blank=True, max_length=420, verbose_name='Ссылка кнопки (блок с фоном под услугами)'),
        ),
        migrations.AddField(
            model_name='about',
            name='promo_middle',
            field=models.CharField(blank=True, max_length=420, verbose_name='Центральная крупная надпись (блок с фоном под услугами)'),
        ),
        migrations.AddField(
            model_name='about',
            name='promo_top',
            field=models.CharField(blank=True, max_length=420, verbose_name='Верхняя надпись (блок с фоном под услугами)'),
        ),
    ]