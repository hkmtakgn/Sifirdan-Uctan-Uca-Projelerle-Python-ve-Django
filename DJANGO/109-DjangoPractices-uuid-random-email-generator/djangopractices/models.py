from django.db import models

# Create your models here.

from django.db.models.functions import Now
from django.core.validators import RegexValidator

nickname_validator = RegexValidator(
    regex=r'^[a-z]{1,10}$',
    message=
    "Nickname sadece küçük harf ile oluşmalı ve en fazla 10 karakter uzunluğunda olmalıdır!"
)


def email_generator():
    import random
    import uuid
    from djangopractices.models import AnonimUser
    email_1 = f"anonymouse{int(random.randint(1,100))}@gmail.com"
    email_2 = f"anonymouse{int(random.randint(1,100))}-{uuid.uuid4().hex[:8]}@gmail.com"

    if not AnonimUser.objects.filter(email=email_1).exists():
        return email_2
    else:
        return email_1


class AnonimUser(models.Model):
    nickname = models.CharField(max_length=100,
                                null=False,
                                blank=False,
                                validators=[nickname_validator])
    email = models.EmailField(blank=True, null=True, default=email_generator)
    created_at = models.DateTimeField(db_default=Now())
