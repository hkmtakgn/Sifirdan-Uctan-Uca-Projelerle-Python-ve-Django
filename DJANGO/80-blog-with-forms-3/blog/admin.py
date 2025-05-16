from django.contrib import admin
from blog.models import post_model
# Register your models here.


@admin.register(post_model)
class PostAdmin(admin.ModelAdmin):
  list_display = ["title", "created_at", "updated_at"]
