# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-18 13:43
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0006_about_promo_block'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='promo_block',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='Промо-блок(после услуг. Если нужно вместо заставки со счетчиками. )'),
        ),
    ]