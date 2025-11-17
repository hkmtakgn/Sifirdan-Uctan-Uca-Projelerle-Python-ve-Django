from django.db import models

# Create your models here.


from django.db.models import F

class SquareCalc (models.Model):
    side = models.IntegerField ()
    area = models.GeneratedField (
        expression = F ("side") * F ("side"),
        output_field = models.BigIntegerField (),
        db_persist = True,
    )

