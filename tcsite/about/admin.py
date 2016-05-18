from django.contrib import admin
from adminsortable.admin import NonSortableParentAdmin, SortableStackedInline

from contacts.admin import LimitedAdmin

from .models import About, Member, Review, Brand, AboutMetaTags, Service

class MemberInline(SortableStackedInline):
    model = Member
    extra = 0

class ClientReviewInline(SortableStackedInline):
    model = Review
    extra = 0

class BrandInline(SortableStackedInline):
    model = Brand
    extra = 0

class ServiceInline(SortableStackedInline):
    model = Service
    extra = 0

class AboutAdmin(NonSortableParentAdmin, LimitedAdmin):
    inlines = [ServiceInline, MemberInline, ClientReviewInline, BrandInline]


admin.site.register(About, AboutAdmin)
admin.site.register(AboutMetaTags, LimitedAdmin)