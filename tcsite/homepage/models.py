from django.db import models
from adminsortable.models import SortableMixin


class CarouselObj(models.Model):
    image = models.ImageField('Картинка 1600x1066', upload_to='home/carousel_images')
    toptitle=models.CharField('Верхняя надпись',max_length=49,blank=True)
    middletitle=models.CharField('Спедняя надпись(большая)', max_length=49, blank=True)
    bottomtitle=models.CharField('Нижняя надпись', max_length=49, blank=True)
    buttontitle=models.CharField('Надпись на кнопке', max_length=49, blank=True)
    href=models.CharField('Ссылка для кнопки', max_length=49, blank=True)

    class Meta:
        verbose_name = 'Для карусели'
        verbose_name_plural = 'Для карусели'
        ordering = ['the_order']


    # define the field the model should be ordered by
    the_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    def __str__(self):
        return 'Для карусели: ' + self.toptitle


class TopVideo(models.Model):
    title=models.CharField('Заголовок', max_length=49,blank=True)
    slogan=models.CharField('Девиз', max_length=49, blank=True)
    video_id=models.CharField('Видео (код ютуба)', max_length=49, blank=True)
    button=models.CharField('Надпись на кнопке', max_length=49, blank=True)
    href=models.CharField('Сылка кнопки', max_length=49, blank=True)

    class Meta:
        verbose_name = 'Видео-заставка'
        verbose_name_plural = 'Видео-заставка'

    def __str__(self):
        return 'Видео-заставка: ' + self.title
