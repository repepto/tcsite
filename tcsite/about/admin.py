from django.contrib import admin

from contacts.admin import LimitedAdmin

from adminsortable.admin import NonSortableParentAdmin, SortableStackedInline

from .models import About, Member, Review, Brand

class MemberInline(SortableStackedInline):
    model = Member
    extra = 0

class ClientReviewInline(SortableStackedInline):
    model = Review
    extra = 0

class BrandInline(SortableStackedInline):
    model = Brand
    extra = 0

class AboutAdmin(NonSortableParentAdmin, LimitedAdmin):
    inlines = [MemberInline, ClientReviewInline, BrandInline]


admin.site.register(About, AboutAdmin)