from django.db import models
from adminsortable.models import SortableMixin

class About(models.Model):
    preview_image = models.ImageField()
    title = models.CharField(max_length=49)
    slogan = models.TextField(blank=True)

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About'
        ordering = ['the_order']

    the_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    def __str__(self):
        return "About"

class TeamMember(SortableMixin):
    about = models.ForeignKey(About, on_delete=models.CASCADE)
    image = models.ImageField()
    name = models.CharField(max_length=49)
    position = models.CharField(max_length=49)

    class Meta:
        verbose_name = 'TeamMember'
        verbose_name_plural = 'TeamMembers'
        ordering = ['member_order']

    member_order =  models.PositiveIntegerField(default=0, editable=False, db_index=True)
