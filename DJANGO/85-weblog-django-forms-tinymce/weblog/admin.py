from django.contrib import admin
from weblog.models import Blog_Post
# Register your models here.


@admin.register(Blog_Post)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = [
        "username",
        "created_date",
        "is_active",
    ]
