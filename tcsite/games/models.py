from django.db import models
from adminsortable.models import SortableMixin
from adminsortable.fields import SortableForeignKey

class AllTags(models.Model):
    tags=models.CharField(max_length=70)
    verbose_name = 'Tags'
    verbose_name_plural = 'Tags'
    def __str__(self):
        return 'Tags'


class Game(SortableMixin):
    preview_image = models.ImageField()
    promo_image = models.ImageField()
    name=models.CharField(max_length=49)
    slogan=models.CharField(max_length=49, blank=True)
    top_title=models.CharField(max_length=49, blank=True)
    top_description_italic=models.TextField(blank=True)
    top_description=models.TextField(blank=True)
    video_id=models.CharField(max_length=49, blank=True)
    midlle_title=models.CharField(max_length=49, blank=True)
    middle_description=models.TextField(blank=True)
    bottom_title=models.CharField(max_length=49, blank=True)
    bottom_description=models.TextField(blank=True)
    client=models.CharField(max_length=49, blank=True)
    tags=models.CharField(max_length=70, blank=True)

    class Meta:
        verbose_name = 'Game'
        verbose_name_plural = 'Game objects'
        ordering = ['game_order']

    # define the field the model should be ordered by
    game_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    def __str__(self):
        return self.name


class Screenshot(SortableMixin):
    game = SortableForeignKey(Game) #, on_delete=models.CASCADE
    screenshot_image=models.ImageField()

    class Meta:
        verbose_name = 'ScreenShot'
        verbose_name_plural = 'ScreenShots'
        ordering = ['screenshot_order']

    screenshot_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    def __str__(self):
        return 'Screenshot: 1000x600'

class TopImage(models.Model):
    image=models.ImageField("Top image")

    def __str__(self):
        return 'Top image: 1000x600'