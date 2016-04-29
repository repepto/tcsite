from django.db import models
from adminsortable.models import SortableMixin


class CarouselObj(models.Model):
    image = models.ImageField()
    toptitle=models.CharField(max_length=49,blank=True)
    middletitle=models.CharField(max_length=49, default='мастерская №8')
    bottomtitle=models.CharField(max_length=49, blank=True)
    buttontitle=models.CharField(max_length=49, blank=True)
    href=models.CharField(max_length=49, blank=True)

    class Meta:
        verbose_name = 'CarouselObj'
        verbose_name_plural = 'CarouselObj'
        ordering = ['the_order']


    # define the field the model should be ordered by
    the_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    def __str__(self):
        return 'Carousel object'
