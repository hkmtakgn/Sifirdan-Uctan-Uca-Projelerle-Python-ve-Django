from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Category (models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from="title",unique=True)
    is_active = models.BooleanField(default=False)

    def __str__ (self):
        return self.title
    
    def get_absolute_url (self):
        return reverse (
            "category_views",
            kwargs={
                "category_slug":self.slug,
            }
        )
    
class Tag (models.Model):
    title = models.CharField (max_length=200)
    slug = AutoSlugField (populate_from='title',unique=True)
    is_active = models.BooleanField (default=False)

    def __str__ (self):
        return self.title
    
    def get_absolute_url (self):
        return reverse (
            'tag_views',
            kwargs={
                "tag_slug":self.slug,
            }
        )

   


class Todo (models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    tag = models.ManyToManyField (Tag)
    content = models.TextField(blank=True,null=True)
    is_active = models.BooleanField (default=False)

    def __str__ (self):
        return self.title
    
    def get_absolute_url (self):
        return reverse (
            "todo_detail",
            kwargs= {
                "id":self.pk,
            }
        )


    
    def get_absolute_url_todo_in_cat (self):
        return reverse (
            "view_todo_in_category",
            kwargs={
                "id":self.pk,
                "category_slug":self.category.slug,
            }
        )

