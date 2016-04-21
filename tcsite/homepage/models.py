from django.db import models
from adminsortable.models import SortableMixin


class CarouselObj(SortableMixin):
    image = models.ImageField()
    toptitle=models.CharField(max_length=49, default='game design company')
    middletitle=models.CharField(max_length=49, default='tabletcrushers')
    bottomtitle=models.CharField(max_length=49, default='have fun, folks')
    buttontitle=models.CharField(max_length=49, default='')

    class Meta:
        verbose_name = 'CarouselObj'
        verbose_name_plural = 'CarouselObj'
        ordering = ['the_order']


    # define the field the model should be ordered by
    the_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    def __str__(self):
        return 'Carousel object'
