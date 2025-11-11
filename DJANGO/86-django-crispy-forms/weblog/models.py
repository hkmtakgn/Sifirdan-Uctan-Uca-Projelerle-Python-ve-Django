from django.db import models


class BaseModel(models.Model):
  username = models.CharField(max_length=100)
  content = models.TextField(null=True, blank=True)
  post_img = models.ImageField(upload_to="post_img/")
  is_active = models.BooleanField(default=True)
  created_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    abstract = True


class Blog_Post(BaseModel):

  def __str__(self):
    return self.username
