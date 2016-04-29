from django.contrib import admin

from contacts.admin import LimitedAdmin

from adminsortable.admin import NonSortableParentAdmin, SortableStackedInline

from .models import About, TeamMember

class TeamMemberInline(SortableStackedInline):
    model = TeamMember
    extra = 0

class AboutAdmin(NonSortableParentAdmin, LimitedAdmin):
    inlines = [TeamMemberInline]


admin.site.register(About, AboutAdmin)