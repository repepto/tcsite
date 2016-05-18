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


class Work(SortableMixin):

    top_image = models.ImageField('Верхняя заставка-картинка 1600 на 1066', upload_to='works/top_images')
    name=models.CharField('Название работы (крупное на заставке)', max_length=49)
    preview_image = models.ImageField('Картинка для предпросмотра 800 на 600', upload_to='works/preview_images')
    slogan=models.CharField('Девиз заставки', max_length=140, blank=True)
    tags=models.CharField('Тэги работы', max_length=70, blank=True)

    text0 = RichTextField(blank=True, verbose_name = 'Верхний текстовый блок')
    video_id=models.CharField('Видео (код ютуба)', max_length=49, blank=True)
    text1 = RichTextField(blank=True, verbose_name = 'Средний текстовый блок (под видео)')
    text2 = RichTextField(blank=True, verbose_name = 'Нижний текстовый блок (под каруселью)')
    client=models.CharField('Для клиента: ', max_length=49, blank=True)

    meta_title = models.CharField('Заголовок страницы (тэг <title>, до 70 символов)', max_length=70, blank=True)
    meta_keywords = models.CharField('Ключевые слова через запятую (тэг <keywords>, до 210 символов)', max_length=210, blank=True)
    meta_description = models.CharField('Описание (тэг <description>, до 210 символов)', max_length=210, blank=True)

    class Meta:
        verbose_name = 'Работа'
        verbose_name_plural = '3: Работы'
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
        verbose_name_plural = 'Картинки карусели 1000 на 600'
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
        verbose_name_plural = '1: Заставка для работ'

    def __str__(self):
        return 'Заставка для работ: ' + self.title

class WorksMetaTags(models.Model):
    title = models.CharField('Заголовок страницы (тэг <title>, до 70 символов)', max_length=70, blank=True)
    keywords = models.CharField('Ключевые слова через запятую (тэг <keywords>, до 210 символов)', max_length=210, blank=True)
    description = models.CharField('Описание (тэг <description>, до 210 символов)', max_length=210, blank=True)

    class Meta:
        verbose_name = 'МетаТэги'
        verbose_name_plural = '4: МетаТэги'

    def __str__(self):
        return 'МетаТэги'