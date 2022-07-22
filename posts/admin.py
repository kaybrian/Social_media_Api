from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['owner','description','likes']
    search_fields = ['owner','description','created_at']
    list_filter = ['owner']
