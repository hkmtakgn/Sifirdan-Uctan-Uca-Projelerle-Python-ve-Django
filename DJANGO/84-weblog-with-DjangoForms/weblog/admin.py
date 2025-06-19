from django.contrib import admin
from weblog.models import Blog

# Register your models here.


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
  list_display = [
      "username",
      "department",
      "language",
  ]
