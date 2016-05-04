from django.contrib import admin

from contacts.admin import LimitedAdmin

from adminsortable.admin import NonSortableParentAdmin, SortableStackedInline

from .models import About, Member, Review

class MemberInline(SortableStackedInline):
    model = Member
    extra = 0

class ClientReviewInline(SortableStackedInline):
    model = Review
    extra = 0

class AboutAdmin(NonSortableParentAdmin, LimitedAdmin):
    inlines = [MemberInline, ClientReviewInline]


admin.site.register(About, AboutAdmin)