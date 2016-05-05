from django.db import models
from adminsortable.models import SortableMixin

class About(models.Model):
    top_image = models.ImageField('Top image 1600x1067', upload_to='about/top_image')
    title = models.CharField(max_length=49)
    slogan = models.TextField(blank=True)
    promo_image = models.ImageField('Promo image 1528x576', upload_to='about/promo_image')
    middle_bg = models.ImageField('middle_bg 1600x1066', upload_to='about/middle_bg')

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About'
        ordering = ['the_order']

    the_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    def __str__(self):
        return "About"


class Brand(SortableMixin):
    abjut = models.ForeignKey(About, on_delete=models.CASCADE)
    image = models.ImageField('Logo', upload_to='about/brands')

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'
        ordering = ['brand_order']

    brand_order =  models.PositiveIntegerField(default=0, editable=False, db_index=True)

class Member(SortableMixin):
    about = models.ForeignKey(About, on_delete=models.CASCADE)
    image = models.ImageField('Member photo 600x820', upload_to='about/team_member_photos')
    name = models.CharField(max_length=49)
    position = models.CharField(max_length=49)

    class Meta:
        verbose_name = 'Team member'
        verbose_name_plural = 'Team members'
        ordering = ['member_order']

    member_order =  models.PositiveIntegerField(default=0, editable=False, db_index=True)

class Review(SortableMixin):
    about = models.ForeignKey(About, on_delete=models.CASCADE)
    avatar = models.ImageField('Avatar 100x100', upload_to='about/client_avatars')
    name = models.CharField(max_length=49)
    speech = models.CharField(max_length=210)

    class Meta:
        verbose_name = 'Client review'
        verbose_name_plural = 'Client reviews'
        ordering = ['member_order']

    member_order =  models.PositiveIntegerField(default=0, editable=False, db_index=True)
