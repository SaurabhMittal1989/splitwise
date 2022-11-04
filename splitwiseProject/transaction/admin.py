from django.contrib import admin

from .models import Transaction, TransactionDetail



# Register your models here.

# admin.site.register(Transaction)
# admin.site.register(TransactionDetail)

@admin.register(Transaction, TransactionDetail,)
class UniversalAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]

    def user(self, obj):
        return str("hello")

