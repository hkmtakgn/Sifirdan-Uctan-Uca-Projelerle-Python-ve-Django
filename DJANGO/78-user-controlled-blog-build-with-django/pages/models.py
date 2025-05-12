from django.db import models
from django import forms

# Create your models here.


class login_model (models.Model) :
    username = models.CharField( max_length=100 )
    password = models.CharField( max_length=100 )


class register_model (models.Model) :
    username = models.CharField ( max_length=100 )
    password = models.CharField ( max_length=100 )
    confirm_password = models.CharField( max_length=100)
    email = models.EmailField()
    confirm_email = models.EmailField()

    DEPARTMENTS = [
        ("Admin", "Administrator"),
        ("PY", "Project Manager"),
        ("UX", "User Experience"),
        ("UI", "User Interface"),
    ]

    dept = models.CharField ( max_length=5, choices = DEPARTMENTS, default = DEPARTMENTS[2][0])


class blog_post (models.Model) :
    username = models.CharField ( max_length=100)
    message = models.TextField ( blank = False, null = False )
    avatar = models.ImageField ( upload_to="avatar/")

