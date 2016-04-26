from django.contrib import admin

from .models import Contacts
# Register your models here.

class LimitedAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True

admin.site.register(Contacts, LimitedAdmin)
