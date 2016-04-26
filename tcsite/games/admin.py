from django.contrib import admin

from adminsortable.admin import SortableAdmin

from .models import Game
from .models import Screenshot



class ScreeenshotInline(admin.StackedInline):
    model = Screenshot

class SortableAdminClass(SortableAdmin):
    fieldsets = [
        ('Preview image: 800x600', {'fields' : ['preview_image']}),
        ('Promo image: 1000x600', {'fields' : ['promo_image']}),
        (None, {'fields' : ['name']}),
        (None, {'fields' : ['slogan']}),
        (None, {'fields' : ['top_title']}),
        (None, {'fields' : ['top_description_italic']}),
        (None, {'fields' : ['top_description']}),
        (None, {'fields' : ['video_id']}),
        (None, {'fields' : ['midlle_title']}),
        (None, {'fields' : ['middle_description']}),
        (None, {'fields' : ['bottom_title']}),
        (None, {'fields' : ['bottom_description']}),
        (None, {'fields' : ['client']}),
        (None, {'fields' : ['tags']}),
    ]
    inlines = [ScreeenshotInline]






class ScreenshotAdmin(admin.ModelAdmin):
    fields=['screenshot_image']

admin.site.register(Game, SortableAdminClass)