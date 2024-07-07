from django.contrib import admin
from main.models import *


@admin.register(RankModel)
class RankModelAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['full_name']
    list_display_links = ['full_name']
    search_fields = ['full_name']


@admin.register(MessageModel)
class MessageModelAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'email']
    list_display_links = ['user_name', 'email']
    list_filter = ['created_at']
