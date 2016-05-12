from django.db import models
from django.contrib import admin

# Create your models here.
class Contacts(models.Model):
    map_adress = models.CharField('адрес для карты', max_length=140)
    adress = models.CharField('адрес', max_length=154)
    email = models.CharField('email', max_length=42)
    phone = models.CharField('телефон', max_length=21)
    slogan = models.CharField(max_length=700, blank=True, verbose_name = 'Девиз')

    class Meta:
        verbose_name = 'Контактная инфа'
        verbose_name_plural = 'Контактная инфа'

    def __str__(self):
        return 'Контактная инфа'
