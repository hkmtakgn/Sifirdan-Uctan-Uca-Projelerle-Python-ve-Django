from django.db import models

# Create your models here.

class login_model (models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    

class register_model (models.Model):
    username = models.CharField (max_length=100)
    password = models.CharField (max_length = 100)
    confirm_password = models.CharField(max_length=100)
    email = models.EmailField()
    confirm_email = models.EmailField()
    
    DEPARTMENTS = [
        ("Admin","Administrator"),
        ("CAO","Baş Analiz Sorumlusu veya Baş İdari Sorumlu"),
        ("MD","Genel Müdür"),
        ("SUPR","Süpervizör"),
        ("UX","User Experience"),
        ("IX","Interface Experience"),
        ("PWA","Progressive Web App"),
        ("SDK","Software Development Kit"),
        ("RWD","Responsive Web Design"),
        ("SQL","Structured Query Language"),
        ("IDE","Integrated Development Environment"),
    ]

    dept = models.CharField(max_length=5, choices=DEPARTMENTS, default=DEPARTMENTS[0][0])
    

class add_story_model (models.Model):
    username = models.CharField ( max_length=100, null=False, blank=False )
    post_content = models.TextField(null=False, blank=False)

    DEPARTMENTS = [
        ("Admin","Administrator"),
        ("CAO","Baş Analiz Sorumlusu veya Baş İdari Sorumlu"),
        ("MD","Genel Müdür"),
        ("SUPR","Süpervizör"),
        ("UX","User Experience"),
        ("IX","Interface Experience"),
        ("PWA","Progressive Web App"),
        ("SDK","Software Development Kit"),
        ("RWD","Responsive Web Design"),
        ("SQL","Structured Query Language"),
        ("IDE","Integrated Development Environment"),
    ]

    dept = models.CharField(max_length=5, choices=DEPARTMENTS, default=DEPARTMENTS[0][1])

    avatar = models.ImageField ( upload_to="avatar/", null=False, blank=False )
    
 
