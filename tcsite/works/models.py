﻿from django.db import models
from adminsortable.models import SortableMixin
from adminsortable.fields import SortableForeignKey

class AllTags(models.Model):
    tags=models.CharField('Тэги через "," без пробелов', max_length=140)
    verbose_name = 'Тэги'
    verbose_name_plural = 'Тэги'

    class Meta:
        verbose_name = 'Тэги для подменю'
        verbose_name_plural = 'Тэги для подменю'

    def __str__(self):
        return 'Тэги: ' + self.tags


class Work(SortableMixin):

    top_image = models.ImageField('Картинка-заставка 1600 на 1066', upload_to='works/top_images')
    name=models.CharField('Название работы (крупное на заставке)', max_length=49)
    preview_image = models.ImageField('Картинка предпросмотра 800 на 600', upload_to='works/preview_images')
    slogan=models.CharField('Девиз заставки', max_length=49, blank=True)
    top_title=models.CharField('Заголовок 1', max_length=49, blank=True)
    top_description_italic=models.TextField('Текст - девиз (наклонный) 1', blank=True)
    top_description=models.TextField('Текст 1', blank=True)
    video_id=models.CharField('Видео (код ютуба)', max_length=49, blank=True)
    midlle_title=models.CharField('Заголовок 2 (под видео)',max_length=49, blank=True)
    middle_description=models.TextField('Текст 2 (под видео)', blank=True)
    bottom_title=models.CharField('Заголовок 3 (под каруселью)', max_length=49, blank=True)
    bottom_description=models.TextField('Текст 3 (под каруселью)', blank=True)
    client=models.CharField('Для клиента: ', max_length=49, blank=True)
    tags=models.CharField('Тэги работы', max_length=70, blank=True)

    class Meta:
        verbose_name = 'Работа'
        verbose_name_plural = 'Работы'
        ordering = ['work_order']

    # define the field the model should be ordered by
    work_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    def __str__(self):
        return "Работа: " + self.name


class Screenshot(SortableMixin):
    game = SortableForeignKey(Work) #, on_delete=models.CASCADE
    screenshot_image=models.ImageField('Картинка 1000 на 600', upload_to='works/instance')

    class Meta:
        verbose_name = 'Картинка 1000 на 600'
        verbose_name_plural = 'Картинки 1000 на 600'
        ordering = ['screenshot_order']

    screenshot_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    def __str__(self):
        return 'Картинка 1000x600'

class Media(models.Model):
    image=models.ImageField('Картинка 1600 на 1060', upload_to='works/main_top_image')
    title=models.CharField('Заголовок', max_length=49, blank=True)
    slogan=models.CharField('Девиз', max_length=140, blank=True)

    class Meta:
        verbose_name = 'Заставка для работ'
        verbose_name_plural = 'Заставка для работ'

    def __str__(self):
        return 'Заставка для работ'