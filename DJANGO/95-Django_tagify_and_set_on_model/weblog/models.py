from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class BaseModel(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
  title = models.CharField(max_length=100)
  content = models.TextField(blank=True, null=True)
  is_active = models.BooleanField(default=False)

  class Meta:
    abstract = True


class Tag(models.Model):
  title = models.CharField(max_length=100)
  is_active = models.BooleanField(default=True)

  def __str__(self):
    return self.title


class Post(BaseModel):
  addTag = models.CharField(max_length=100)
  tag = models.ManyToManyField(Tag)
  favs = models.BooleanField(default=False)
  post_img = models.ImageField(upload_to="post-img/", blank=True, null=True)

  def __str__(self):
    return self.title
