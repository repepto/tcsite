from django.db import models
from adminsortable.models import SortableMixin


class Game(SortableMixin):
    preview_image = models.ImageField()
    promo_image = models.ImageField()
    name=models.CharField(max_length=49, default='')
    slogane=models.CharField(max_length=49, default='')
    top_title=models.CharField(max_length=49, default='')
    top_description_italic=models.TextField(default='')
    top_description=models.TextField(default='')
    video_id=models.CharField(max_length=49, default='')
    midlle_title=models.CharField(max_length=49, default='')
    middle_description=models.TextField(default='')
    bottom_title=models.CharField(max_length=49, default='')
    bottom_description=models.TextField(default='')
    client=models.CharField(max_length=49, default='')
    tags=models.CharField(max_length=70, default='')

    class Meta:
        verbose_name = 'Games'
        verbose_name_plural = 'Game objects'
        ordering = ['the_order']


    # define the field the model should be ordered by
    the_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    def __str__(self):
        return self.name


class Screenshot(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    screenshot_image=models.ImageField()
    def __str__(self):
        return 'Screenshot: 1000x600'