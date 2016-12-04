# -*- coding: utf-8 -*-

from django.db import models
from adminsortable.models import SortableMixin
from ckeditor.fields import RichTextField

class About(models.Model):
    top_image = models.ImageField('Верхняя картинка 1600x1067', upload_to='about/top_image')
    title = models.CharField('Заголовок', max_length=70)
    slogan = models.CharField('Девиз', max_length=420, blank=True)
    promo_image = models.ImageField('Картинка (наши услуги) 1528x576', upload_to='about/promo_image', blank=True)
    middle_bg = models.ImageField('Фон под иконками достижений 1600x1066', upload_to='about/middle_bg', blank=True)
    service_slogan = models.CharField('Девиз услуг', max_length=420, blank=True)
    team_slogan = models.CharField('Девиз команды', max_length=420, blank=True)

    promo_top =  models.CharField('Верхняя надпись (блок с фоном под услугами. '
                                  'Если поля блока оставить пустыми, будет заставка со счетчиками)', max_length=140, blank=True)
    promo_middle =  models.CharField('Центральная крупная надпись (блок с фоном под услугами)', max_length=140, blank=True)
    promo_bottom =  models.CharField('Нижняя надпись (блок с фоном под услугами)', max_length=140, blank=True)
    promo_italic =  models.CharField('Наклонный текст (блок с фоном под услугами)', max_length=420, blank=True)
    promo_buttton =  models.CharField('Надпись на кнопке (блок с фоном под услугами)', max_length=420, blank=True)
    promo_href =  models.CharField('Ссылка кнопки (блок с фоном под услугами)', max_length=420, blank=True)

    class Meta:
        verbose_name = 'О мастерской'
        verbose_name_plural = '1: О мастерской'
        ordering = ['the_order']

    the_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    def __str__(self):
        return "О мастерской"

class Service(SortableMixin):
    about = models.ForeignKey(About, on_delete=models.CASCADE)
    title = models.CharField('Заголовок', max_length=70)
    text = RichTextField(verbose_name = 'Текст')
    ico_alias = models.CharField('Код текстовой иконки(коды см. тут: http://rhythm.nikadevs.com/content/icons-et-line)', max_length=21, blank=True)
    ico_img = models.ImageField('Иконка 80х80, ввместо текстовой иконки, если нужно', upload_to='about/services_ico', blank=True)

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        ordering = ['s_order']

    s_order =  models.PositiveIntegerField(default=0, editable=False, db_index=True)


class Brand(SortableMixin):
    about = models.ForeignKey(About, on_delete=models.CASCADE)
    image = models.ImageField('Логотип', upload_to='about/brands')

    class Meta:
        verbose_name = 'Логотип'
        verbose_name_plural = 'Логотипы'
        ordering = ['brand_order']

    brand_order =  models.PositiveIntegerField(default=0, editable=False, db_index=True)

class Member(SortableMixin):
    about = models.ForeignKey(About, on_delete=models.CASCADE)
    image = models.ImageField('Фотка 600x820', upload_to='about/team_member_photos')
    name = models.CharField('Имя' ,max_length=49)
    position = models.CharField('Должность', max_length=49)

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        ordering = ['member_order']

    member_order =  models.PositiveIntegerField(default=0, editable=False, db_index=True)

class Review(SortableMixin):
    about = models.ForeignKey(About, on_delete=models.CASCADE)
    avatar = models.ImageField('Аватарка 100x100', upload_to='about/client_avatars')
    name = models.CharField('Имя', max_length=49)
    speech = models.CharField('Слова', max_length=210)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['member_order']

    member_order =  models.PositiveIntegerField(default=0, editable=False, db_index=True)

class AboutMetaTags(models.Model):
    title = models.CharField('Заголовок страницы (тэг <title>, до 70 символов)', max_length=70, blank=True)
    keywords = models.CharField('Ключевые слова через запятую (тэг <keywords>, до 210 символов)', max_length=210, blank=True)
    description = models.CharField('Описание (тэг <description>, до 210 символов)', max_length=210, blank=True)

    class Meta:
        verbose_name = 'МетаТэги'
        verbose_name_plural = '2: МетаТэги'

    def __str__(self):
        return 'МетаТэги'
