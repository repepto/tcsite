from django.db import models


class Carousel(models.Model):
    image = models.ImageField()
    toptitle=models.CharField(max_length=49, default='game design company')
    middletitle=models.CharField(max_length=49, default='tabletcrushers')
    bottomtitle=models.CharField(max_length=49, default='have fun, folks')
    buttontitle=models.CharField(max_length=49, default='')
    def __str__(self):
        return 'Carousel element'
