from django.contrib import admin
from .models import User 


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_dislay = ['first_name','last_name','email','username','phone_number']
    list_filter = ['first_name','email','phone_number']
    search_fields = ['email','phone_number','username']


