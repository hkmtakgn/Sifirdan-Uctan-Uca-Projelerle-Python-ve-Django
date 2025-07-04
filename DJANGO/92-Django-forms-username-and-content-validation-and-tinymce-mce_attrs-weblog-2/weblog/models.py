from django.db import models

# Create your models here.


class Post(models.Model):
  title = models.CharField(max_length=100)
  content = models.TextField(blank=True, null=True)
  post_img = models.ImageField(upload_to="post-img/")
  created_date = models.DateTimeField(auto_now_add=True)
  is_active = models.BooleanField(default=True)

  def __str__(self):
    return self.title
