from django.db import models
from autoslug import AutoSlugField
import datetime


class Category (models.Model):
    title = models.CharField(max_length=200)
    is_active = models.BooleanField(default=False)
    slug = AutoSlugField(populate_from="title",unique=True)

    def __str__ (self):
        return self.title


class Todo(models.Model):
    category = models.ForeignKey(Category,models.SET_NULL,null=True)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=False)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__ (self):
        return self.title
    
    
