from django.contrib import admin
from weblog.models import Post

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  list_display = [
      "user",
      "title",
      "content",
      "is_active",
  ]
