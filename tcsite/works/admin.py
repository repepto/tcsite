from django.contrib import admin
from adminsortable.admin import SortableAdmin, SortableStackedInline
from .models import Work, Screenshot, AllTags, Media, WorksMetaTags
from contacts.admin import LimitedAdmin



class ScreenshotInline(SortableStackedInline):
    model = Screenshot
    extra = 0

class SortableAdminClass(SortableAdmin):
    inlines = [ScreenshotInline]

admin.site.register(Work, SortableAdminClass)
admin.site.register(AllTags, LimitedAdmin)
admin.site.register(Media, LimitedAdmin)
admin.site.register(WorksMetaTags, LimitedAdmin)