from django.contrib import admin
from .models import *


@admin.register(OpportunityModel)
class OpportunityAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']


@admin.register(HostingModel)
class HostingAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'real_price', 'sale', 'discount', 'created_at']
    list_display_links = ['name', 'price', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'price']
    autocomplete_fields = ['opportunity']
    readonly_fields = ['real_price', 'sale']
