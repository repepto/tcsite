from django.db import models

from adminsortable.models import SortableMixin
from adminsortable.fields import SortableForeignKey
from ckeditor.fields import RichTextField

class AllTags(models.Model):
    tags=models.CharField('Тэги через "," без пробелов', max_length=140)
    verbose_name = 'Тэги'
    verbose_name_plural = 'Тэги'

    class Meta:
        verbose_name = 'Тэги для подменю'
        verbose_name_plural = '2: Тэги для подменю'

    def __str__(self):
        return 'Тэги: ' + self.tags

class Post(SortableMixin):

    top_image = models.ImageField(upload_to='blog/top_image', verbose_name = 'Заставка')
    title=models.CharField(max_length=49, verbose_name = 'Заголовок заставки')
    slogan=models.CharField(max_length=140, blank=True, verbose_name = 'Девиз')
    txt = models.TextField(blank=True, verbose_name = 'Предварительный текст')
    tags = models.CharField(max_length=140, blank=True, verbose_name = 'Тэги через "," без пробелов')

    meta_title = models.CharField('Заголовок страницы (тэг <title>, до 70 символов)', max_length=70, blank=True)
    meta_keywords = models.CharField('Ключевые слова через запятую (тэг <keywords>, до 210 символов)', max_length=210, blank=True)
    meta_description = models.CharField('Описание (тэг <description>, до 210 символов)', max_length=210, blank=True)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = '3: Посты'
        ordering = ['post_order']

    post_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    def __str__(self):
        return 'Пост: ' + self.title



class Top(SortableMixin):
    post = SortableForeignKey(Post)

    text = RichTextField(blank=True, verbose_name = 'Текст')
    video = models.CharField(max_length=14, blank=True, verbose_name = 'Видео ID(youtube)')
    image = models.ImageField(upload_to='blog/block', blank=True, verbose_name = 'Картинка')

    class Meta:
        verbose_name = 'Верхний блок'
        verbose_name_plural = 'Верхние блоки, которые над каруселью'
        ordering = ['top_order']

    top_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    def __str__(self):
        return 'Верхний блок'


class Bottom(SortableMixin):
    post = SortableForeignKey(Post)

    text = RichTextField(blank=True, verbose_name = 'Текст')
    video = models.CharField(max_length=14, blank=True, verbose_name = 'Видео ID(youtube)')
    image = models.ImageField(upload_to='blog/block', blank=True, verbose_name = 'Картинка')

    class Meta:
        verbose_name = 'Нижний блок'
        verbose_name_plural = 'Нижние блоки, которые под каруселью'
        ordering = ['b_order']

    b_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    def __str__(self):
        return 'Нижний блок'


class Carousel(SortableMixin):
    post = SortableForeignKey(Post) #, on_delete=models.CASCADE
    image=models.ImageField(upload_to='blog/instance/carousel')

    class Meta:
        verbose_name = 'Картинка 1000 на 600'
        verbose_name_plural = 'Картинки для карусели 1000 на 600'
        ordering = ['i_order']

    i_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    def __str__(self):
        return 'Картинка: 1000x600'

class TopMedia(models.Model):
    top_image = models.ImageField('Картинка 1600 на 1060', upload_to='blog/media')
    title=models.CharField('Заголвок', max_length=49, blank=True)
    slogan=models.CharField('Девиз', max_length=140, blank=True)

    class Meta:
        verbose_name = 'Заставка для блога'
        verbose_name_plural = '1: Заставка для блога'

    def __str__(self):
        return 'Заставка для блога'

class BlogMetaTags(models.Model):
    title = models.CharField('Заголовок страницы (тэг <title>, до 70 символов)', max_length=70, blank=True)
    keywords = models.CharField('Ключевые слова через запятую (тэг <keywords>, до 210 символов)', max_length=210, blank=True)
    description = models.CharField('Описание (тэг <description>, до 210 символов)', max_length=210, blank=True)

    class Meta:
        verbose_name = 'МетаТэги'
        verbose_name_plural = '4: МетаТэги'

    def __str__(self):
        return 'МетаТэги'