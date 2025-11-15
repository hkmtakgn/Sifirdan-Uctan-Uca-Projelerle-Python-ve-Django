from django.db import models
from django.db.models.functions import Now

Hobby = models.TextChoices("hobby",
                           "Table_Tennis Basketball Bowling Volleyball")

Skills = [("Front End", [("js", "JavaScript"), ("react", "React")]),
          ("Back End", [("py", "Python"), ("dj", "Django")])]

db = {"Data Base": {"sql": "Sql", "psql": "Postgre Sql"}}


class anon_user(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    hobbies = models.CharField(max_length=20, choices=Hobby)
    skills = models.CharField(max_length=20, choices=Skills)
    data_base = models.CharField(max_length=20, choices=db)
    created_at = models.DateTimeField(db_default=Now())

    def __str__(self):
        return self.name
