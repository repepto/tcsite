from django.contrib import admin

from adminsortable.admin import SortableAdmin, SortableStackedInline

from .models import Work, Screenshot, AllTags, Media

from contacts.admin import LimitedAdmin



class ScreenshotInline(SortableStackedInline):
    model = Screenshot
    extra = 0

class SortableAdminClass(SortableAdmin):
    fieldsets = [
        (None, {'fields' : ['preview_image']}),
        (None, {'fields' : ['top_image']}),
        (None, {'fields' : ['name']}),
        (None, {'fields' : ['slogan']}),
        (None, {'fields' : ['text0']}),
        (None, {'fields' : ['video_id']}),
        (None, {'fields' : ['text1']}),
        (None, {'fields' : ['text2']}),
        (None, {'fields' : ['client']}),
        (None, {'fields' : ['tags']}),
    ]

    inlines = [ScreenshotInline]

admin.site.register(AllTags, LimitedAdmin)

admin.site.register(Media, LimitedAdmin)

admin.site.register(Work, SortableAdminClass)