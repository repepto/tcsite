from django.contrib import admin

from adminsortable.admin import SortableAdmin

from .models import CarouselObj

#from .models import CarouselObj

class SortableAdminClass(SortableAdmin):
    """Any admin options you need go here"""

admin.site.register(CarouselObj, SortableAdminClass)
