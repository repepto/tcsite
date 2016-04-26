from django.db import models
from django.contrib import admin

# Create your models here.
class Contacts(models.Model):
    latitude = models.CharField('The field', max_length=100)
    longitude = models.CharField('The field', max_length=100)