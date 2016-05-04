from django.contrib import admin

from adminsortable.admin import SortableAdmin

from contacts.admin import LimitedAdmin

from .models import CarouselObj, TopVideo

#from .models import CarouselObj

class SortableAdminClass(SortableAdmin):
    """Any admin options you need go here"""

admin.site.register(CarouselObj, SortableAdminClass)

admin.site.register(TopVideo, LimitedAdmin)
