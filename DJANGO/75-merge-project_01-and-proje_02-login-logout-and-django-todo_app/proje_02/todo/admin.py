from django.contrib import admin
from todo.models import Todo

# Register your models here.

@admin.register (Todo)
class TodoAdmin (admin.ModelAdmin):
    pass
