from django.contrib import admin

from weblog.models import Blog_Post


@admin.register(Blog_Post)
class AdminPost(admin.ModelAdmin):
  list_display = [
      "username",
      "is_active",
      "created_at",
  ]
