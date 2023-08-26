from django.contrib import admin
from .models import *




# class CustomerInvoicesInline(admin.TabularInline):
#     model = CustomerInvoices
    
# class CustomerAdmin(admin.ModelAdmin):
#     inlines = [CustomerInvoicesInline]
    
admin.site.register(Customer)
admin.site.register(Invoice)