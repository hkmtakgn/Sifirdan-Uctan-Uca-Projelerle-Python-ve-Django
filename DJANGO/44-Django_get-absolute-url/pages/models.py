from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse


class Category (models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from="title",unique=True)
    is_active = models.BooleanField(default=False)
    
    def __str__ (self):
        return self.title


class Todo (models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category,models.SET_NULL,null=True)
    content = models.TextField(blank=True,null=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__ (self):
        return self.title
    
    def get_absolute_url (self):
        return reverse (
            "todo_detail",
            kwargs={
                "id":self.pk
            }
        )
