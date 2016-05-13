from django.db import models
from adminsortable.models import SortableMixin
from PIL import Image as Img
from io import StringIO
from  io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

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
        return self.toptitle + '; ' + self.middletitle + '; ' + self.bottomtitle
    """
    #custom image quality
    def save(self, *args, **kwargs):
        if self.image:
            output = BytesIO()
            img = Img.open(self.image)
            img.save(output, 'JPEG', quality=70)
            output.seek(0)
            self.image = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.image.name.split('.')[0], 'image/jpeg', output.tell(), None)
        super(CarouselObj, self).save(*args, **kwargs)
    """


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
