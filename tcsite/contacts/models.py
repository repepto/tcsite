# -*- coding: utf-8 -*-

from django.db import models
from django.contrib import admin

# Create your models here.
class Contacts(models.Model):
    map_adress = models.CharField('адрес для карты', max_length=140, default='Киев. Украина')
    adress = models.CharField('адрес', max_length=154)
    email = models.CharField('email', max_length=42)
    phone = models.CharField('телефон', max_length=21)
    slogan = models.CharField(max_length=700, blank=True, verbose_name = 'Девиз')

    class Meta:
        verbose_name = 'Контактная инфа'
        verbose_name_plural = '1: Контактная инфа'

    def __str__(self):
        return 'Контактная инфа'

class SocialLinks(models.Model):
    facebook = models.CharField('Ссылка на facebook', max_length=70, blank=True)
    twitter = models.CharField('Ссылка на twitter', max_length=70, blank=True)
    instagram = models.CharField('Ссылка на instagram', max_length=70, blank=True)
    behance = models.CharField('Ссылка на behance', max_length=70, blank=True)
    dribble = models.CharField('Ссылка на dribble', max_length=70, blank=True)

    class Meta:
        verbose_name = 'Ссылки на соц. сайты'
        verbose_name_plural = '2: Ссылки на соц. сайты'

    def __str__(self):
        return 'Ссылки на соц. сайты'
