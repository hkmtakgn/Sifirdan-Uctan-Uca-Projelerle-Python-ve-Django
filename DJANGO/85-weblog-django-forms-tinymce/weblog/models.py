from django.db import models
from tinymce import models as tinymce_model
# Create your models here.


class BaseModel(models.Model):
  username = models.CharField(max_length=100)
  # content = models.TextField(null=True, blank=True)
  content = tinymce_model.HTMLField(blank=True, null=True)
  created_date = models.DateTimeField(auto_now_add=True)
  post_img = models.ImageField(upload_to="post_img/")
  is_active = models.BooleanField(default=True)

  class Meta:
    abstract = True


class Blog_Post(BaseModel):

  def __str__(self):
    return self.username
