from django.db import models
from adminsortable.models import SortableMixin


class CarouselObj(models.Model):
    image = models.ImageField('Image 1600x1066', upload_to='home/carousel_images')
    toptitle=models.CharField('Top title',max_length=49,blank=True)
    middletitle=models.CharField('Middle title', max_length=49, blank=True)
    bottomtitle=models.CharField('Bottom title', max_length=49, blank=True)
    buttontitle=models.CharField('Button lettering', max_length=49, blank=True)
    href=models.CharField('Button href', max_length=49, blank=True)

    class Meta:
        verbose_name = 'Carousel object'
        verbose_name_plural = 'Carousel objects'
        ordering = ['the_order']


    # define the field the model should be ordered by
    the_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    def __str__(self):
        return 'Carousel object'


class TopVideo(models.Model):
    title=models.CharField(max_length=49,blank=True)
    slogan=models.CharField(max_length=49, blank=True)
    video_id=models.CharField(max_length=49, blank=True)
    button=models.CharField(max_length=49, blank=True)
    href=models.CharField(max_length=49, blank=True)

    class Meta:
        verbose_name = 'top video object'
        verbose_name_plural = 'top video object'

    def __str__(self):
        return 'Top video object'
