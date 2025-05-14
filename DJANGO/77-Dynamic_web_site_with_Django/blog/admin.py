from django.contrib import admin
from blog.models import Post,Category,Profile

# Register your models here.


@admin.register (Post)
class PostAdmin (admin.ModelAdmin):
    pass

@admin.register (Category)
class PostAdmin (admin.ModelAdmin):
    pass

@admin.register (Profile)
class PostProfileAdmin (admin.ModelAdmin):
    pass

