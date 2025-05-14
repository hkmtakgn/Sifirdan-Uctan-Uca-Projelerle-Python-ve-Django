from django.db import models
from autoslug import AutoSlugField
from tinymce import models as TinymceModel

# Create your models here.


class Developer (models.Model):
    title = models.CharField(max_length=100)
    slug = AutoSlugField (populate_from='title',unique=True)
    content = TinymceModel.HTMLField (blank=True,null=True)
    dev_img = models.ImageField (upload_to="dev_img/")
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title

