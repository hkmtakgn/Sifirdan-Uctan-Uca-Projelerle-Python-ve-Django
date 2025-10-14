from django.db import models
from autoslug import AutoSlugField
from autoslug import AutoSlugField


class Page(models.Model):
    title = models.CharField(max_length=100, unique=True)
    page_slug = AutoSlugField(populate_from="title")
    page_bg_img = models.ImageField(upload_to="page_bg_img",
                                    null=True,
                                    blank=True)
    page_avatar = models.ImageField(upload_to="page_avatar",
                                    null=True,
                                    blank=True)
    content = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Interface_user(models.Model):
    nickname = models.CharField(max_length=100,
                                null=False,
                                blank=False,
                                unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(null=False, blank=False, unique=True)
    password = models.CharField(max_length=100, null=False, blank=False)
    re_password = models.CharField(max_length=100, null=False, blank=False)
    is_active = models.BooleanField(default=True)
    is_online = models.BooleanField(default=True)

    def __str__(self):
        return self.nickname


class Post(models.Model):
    user = models.ForeignKey(Interface_user,
                             on_delete=models.CASCADE,
                             null=False,
                             blank=False)
    slug = AutoSlugField(populate_from="title")
    title = models.CharField(max_length=100)
    content = models.TextField(blank=False, null=False)
    post_img = models.ImageField(upload_to="post_img/", blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class FavPost(models.Model):
    user = models.ForeignKey(Interface_user, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.post.title
