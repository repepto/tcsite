from django.db import models
from adminsortable.models import SortableMixin

class About(models.Model):
    top_image = models.ImageField('Верхняя картинка 1600x1067', upload_to='about/top_image')
    title = models.CharField('Заголовок', max_length=70)
    slogan = models.CharField('Девиз', max_length=420, blank=True)
    promo_image = models.ImageField('Картинка (наши услуги) 1528x576', upload_to='about/promo_image')
    middle_bg = models.ImageField('Фон под иконками достижений 1600x1066', upload_to='about/middle_bg', blank=True)
    service_slogan = models.CharField('Девиз услуг', max_length=420, blank=True)
    team_slogan = models.CharField('Девиз команды', max_length=420, blank=True)

    class Meta:
        verbose_name = 'Салон'
        verbose_name_plural = 'Салон'
        ordering = ['the_order']

    the_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    def __str__(self):
        return "Салон"


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
