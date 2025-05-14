from django.db import models
from autoslug import AutoSlugField

# Create your models here.

class Categories (models.Model):
    title = models.CharField (max_length=200)
    slug = AutoSlugField (populate_from='title',unique=True)
    is_active = models.BooleanField (default=False)

    def __str__ (self):
        return self.title

class Tag (models.Model):
    title = models.CharField (max_length=200)
    slug = AutoSlugField (populate_from='title',unique=True)
    is_active = models.BooleanField (default=False)

    def __str__ (self):
        return self.title



class Developers (models.Model):
    title = models.CharField (max_length=200)
    category = models.ForeignKey (Categories,on_delete=models.SET_NULL,null=True)
    tag = models.ManyToManyField (Tag)
    content = models.TextField (blank=True,null=True)
    is_active = models.BooleanField (default=False)

    def __str__ (self):
        return self.title

