# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-17 21:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('top_image', models.ImageField(upload_to='about/top_image', verbose_name='Верхняя картинка 1600x1067')),
                ('title', models.CharField(max_length=70, verbose_name='Заголовок')),
                ('slogan', models.CharField(blank=True, max_length=420, verbose_name='Девиз')),
                ('promo_image', models.ImageField(upload_to='about/promo_image', verbose_name='Картинка (наши услуги) 1528x576')),
                ('middle_bg', models.ImageField(blank=True, upload_to='about/middle_bg', verbose_name='Фон под иконками достижений 1600x1066')),
                ('service_slogan', models.CharField(blank=True, max_length=420, verbose_name='Девиз услуг')),
                ('team_slogan', models.CharField(blank=True, max_length=420, verbose_name='Девиз команды')),
                ('the_order', models.PositiveIntegerField(db_index=True, default=0, editable=False)),
            ],
            options={
                'verbose_name_plural': 'Салон',
                'verbose_name': 'Салон',
                'ordering': ['the_order'],
            },
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='about/brands', verbose_name='Логотип')),
                ('brand_order', models.PositiveIntegerField(db_index=True, default=0, editable=False)),
                ('about', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='about.About')),
            ],
            options={
                'verbose_name_plural': 'Логотипы',
                'verbose_name': 'Логотип',
                'ordering': ['brand_order'],
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='about/team_member_photos', verbose_name='Фотка 600x820')),
                ('name', models.CharField(max_length=49, verbose_name='Имя')),
                ('position', models.CharField(max_length=49, verbose_name='Должность')),
                ('member_order', models.PositiveIntegerField(db_index=True, default=0, editable=False)),
                ('about', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='about.About')),
            ],
            options={
                'verbose_name_plural': 'Сотрудники',
                'verbose_name': 'Сотрудник',
                'ordering': ['member_order'],
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(upload_to='about/client_avatars', verbose_name='Аватарка 100x100')),
                ('name', models.CharField(max_length=49, verbose_name='Имя')),
                ('speech', models.CharField(max_length=210, verbose_name='Слова')),
                ('member_order', models.PositiveIntegerField(db_index=True, default=0, editable=False)),
                ('about', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='about.About')),
            ],
            options={
                'verbose_name_plural': 'Отзывы',
                'verbose_name': 'Отзыв',
                'ordering': ['member_order'],
            },
        ),
    ]
