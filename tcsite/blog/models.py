from django.db import models

from adminsortable.models import SortableMixin

from adminsortable.fields import SortableForeignKey


class AllTags(models.Model):
    tags=models.CharField(max_length=70)
    verbose_name = 'Tags'
    verbose_name_plural = 'Tags'
    def __str__(self):
        return 'Tags divided by ,'

class Post(SortableMixin):

    top_image = models.ImageField(upload_to='blog/top_image')
    title=models.CharField(max_length=49)
    slogan=models.CharField(max_length=140, blank=True)

    middle_background = models.ImageField(upload_to='blog/middle_bg')

    block1=models.TextField(blank=True)

    video=models.CharField(max_length=21, blank=True)

    image1=models.ImageField(blank=True)

    block2=models.TextField(blank=True)

    image2=models.ImageField(blank=True)

    block3=models.TextField(blank=True)

    image3=models.ImageField(blank=True)

    block3=models.TextField(blank=True)

    tags = models.CharField(max_length=140, blank=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['post_order']

    post_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    def __str__(self):
        return 'Post'


class Carousel(SortableMixin):
    post = SortableForeignKey(Post) #, on_delete=models.CASCADE
    image=models.ImageField(upload_to='blog/instance/carousel')

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'
        ordering = ['i_order']

    i_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    def __str__(self):
        return 'Screenshot: 1000x600'

class TopMedia(models.Model):
    top_image = models.ImageField(upload_to='blog/media')
    title=models.CharField(max_length=49, blank=True)
    slogan=models.CharField(max_length=140, blank=True)
