from django.contrib import admin
from adminsortable.admin import SortableAdmin

from contacts.admin import LimitedAdmin
from .models import CarouselObj, TopVideo, HomeMetaTags

class SortableAdminClass(SortableAdmin):
    """Any admin options you need go here"""

admin.site.register(CarouselObj, SortableAdminClass)
admin.site.register(TopVideo, LimitedAdmin)
admin.site.register(HomeMetaTags, LimitedAdmin)