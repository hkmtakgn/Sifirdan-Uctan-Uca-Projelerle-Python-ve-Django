from django.contrib import admin
from my_weblog.models import PostModel
# Register your models here.


@admin.register(PostModel)
class PostModelAdmin(admin.ModelAdmin):
  list_display = [
      "username",
      "created_at",
      "is_active",
  ]
