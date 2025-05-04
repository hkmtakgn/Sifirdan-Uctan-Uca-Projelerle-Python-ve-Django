from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User

# Create your models here.

class BaseModel (models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    slug = AutoSlugField (populate_from="title",unique=True)
    is_active = models.BooleanField(default=False)

    class Meta:
        abstract = True

class Profile (models.Model):
    user = models.OneToOneField (User, on_delete=models.CASCADE)
    instagram = models.CharField (max_length=200)
    slug = AutoSlugField (populate_from="get_username_for_slug")
    is_active = models.BooleanField(default=False)

    def get_username_for_slug (self):
        return self.user.username

    def __str__ (self):
        return self.user.username


class Category (BaseModel):
    profile = models.ForeignKey (Profile, on_delete=models.CASCADE)
    def __str__(self):
        return self.title


class Post (BaseModel):
    category = models.ForeignKey (Category, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.title
