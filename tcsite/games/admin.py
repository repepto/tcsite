﻿from django.contrib import admin

from adminsortable.admin import SortableAdmin, SortableStackedInline

from .models import Game, Screenshot, AllTags, TopImage

from contacts.admin import LimitedAdmin



class ScreenshotInline(SortableStackedInline):
    model = Screenshot
    extra = 0

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

    inlines = [ScreenshotInline]

admin.site.register(AllTags, LimitedAdmin)

admin.site.register(TopImage, LimitedAdmin)

admin.site.register(Game, SortableAdminClass)