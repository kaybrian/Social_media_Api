from django.contrib import admin
from .models import User, Profile,Message


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_dislay = ['first_name','last_name','email','username','phone_number']
    list_filter = ['first_name','email','phone_number']
    search_fields = ['email','phone_number','username']


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','name','email','phone_number']
    list_filter = ['name','email','created_at']
    search_fields = ['name','email']



@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['sender','recipient','created']
    list_filter = ['sender','recipient']
    search_fields = ['sender','recipient']
