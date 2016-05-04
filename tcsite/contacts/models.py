from django.db import models
from django.contrib import admin

# Create your models here.
class Contacts(models.Model):
    map_adress = models.CharField('map_adress', max_length=140)
    adress = models.CharField('adress', max_length=154)
    email = models.CharField('email', max_length=42)
    phone = models.CharField('phone', max_length=21)