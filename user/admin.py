from django.contrib import admin
from .models import Profile, Message



@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','name','email','phone_number']
    list_filter = ['name','email','created_at']
    search_fields = ['name','email']
    prepopulated_fields = {"slug": ("name",)}



@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['sender','recipient','created']
    list_filter = ['sender','recipient']
    search_fields = ['sender','recipient']
    prepopulated_fields = {"slug": ("subject",)}
