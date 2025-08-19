from django.db import models

# Create your models here.


class BaseModel(models.Model):
  title = models.CharField(max_length=100)
  content = models.TextField(blank=True, null=True)
  is_active = models.BooleanField(default=False)

  class Meta:
    abstract = True


class Post(BaseModel):
  post_img = models.ImageField(upload_to="post-img/", blank=True, null=True)
