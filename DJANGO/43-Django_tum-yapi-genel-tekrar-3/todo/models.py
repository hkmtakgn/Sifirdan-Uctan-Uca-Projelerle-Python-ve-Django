from django.db import models
from autoslug import AutoSlugField

# Create your models here.


class Category (models.Model):
    title = models.CharField(max_length=200)
    is_active = models.BooleanField(default=False)
    slug = AutoSlugField (populate_from="title",unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__ (self):
        return self.title


class Todo (models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category,models.SET_NULL,null=True)
    content = models.TextField(blank=True,null=True)
    mail_address = models.CharField(max_length=200,blank=True,null=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__ (self):
        return self.title


