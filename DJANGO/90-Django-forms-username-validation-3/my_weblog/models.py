from django.db import models

# Create your models here.


class BaseModel(models.Model):
  username = models.CharField(max_length=100)
  content = models.TextField(blank=True, null=True)
  is_active = models.BooleanField(default=True)
  created_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    abstract = True


class PostModel(BaseModel):
  post_img = models.ImageField(upload_to="post-img/")

  def __str__(self):
    return self.username
