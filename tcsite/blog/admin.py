from django.contrib import admin

from adminsortable.admin import SortableAdmin, SortableStackedInline

from contacts.admin import LimitedAdmin

from .models import Post, Carousel, AllTags, TopMedia

class CarouselInline(SortableStackedInline):
    model = Carousel
    extra = 0


class SortableAdminClass(SortableAdmin):

    inlines = [CarouselInline]


admin.site.register(Post, SortableAdminClass)

admin.site.register(AllTags, LimitedAdmin)

admin.site.register(TopMedia, LimitedAdmin)
