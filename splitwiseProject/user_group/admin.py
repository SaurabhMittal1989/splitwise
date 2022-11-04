from django.contrib import admin

from .models import *

# Register your models here.
# admin.site.register(User)
# admin.site.register(Group)
# admin.site.register(GroupDetail)

@admin.register(User, Group,GroupDetail)
class UniversalAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]
