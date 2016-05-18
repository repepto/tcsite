from django.contrib import admin

from adminsortable.admin import SortableAdmin, SortableStackedInline

from contacts.admin import LimitedAdmin

from .models import Post, Carousel, AllTags, TopMedia, Top, Bottom, BlogMetaTags

class CarouselInline(SortableStackedInline):
    model = Carousel
    extra = 0

class TopInline(SortableStackedInline):
    model = Top
    extra = 0

class BottomInline(SortableStackedInline):
    model = Bottom
    extra = 0

class SortableAdminClass(SortableAdmin):
    inlines = [TopInline, CarouselInline, BottomInline]


admin.site.register(Post, SortableAdminClass)
admin.site.register(AllTags, LimitedAdmin)
admin.site.register(TopMedia, LimitedAdmin)
admin.site.register(BlogMetaTags, LimitedAdmin)
