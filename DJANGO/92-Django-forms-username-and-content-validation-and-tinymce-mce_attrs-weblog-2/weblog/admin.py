from django.contrib import admin
from weblog.models import Post

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  list_display = [
      "title",
      "created_date",
      "is_active",
  ]
