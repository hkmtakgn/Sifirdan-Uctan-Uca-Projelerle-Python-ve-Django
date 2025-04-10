from django.db import models
from autoslug import AutoSlugField
from tinymce import models as tinymceModel


# Create your models here.

class Page (models.Model):
    title = models.CharField (max_length=200)
    slug = AutoSlugField (populate_from="title",unique=True)
    bg_image = models.ImageField (upload_to="img/")
    content = tinymceModel.HTMLField (blank=True,null=True)
    is_active = models.BooleanField (default=False)

    def __str__(self):
        return self.title


class Developer (models.Model):
    title = models.CharField (max_length=200)
    content = tinymceModel.HTMLField (blank=True,null=True)
    is_active = models.BooleanField (default=False)

    def __str__(self):
        return self.title

