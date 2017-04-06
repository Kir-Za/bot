from django.db import models
from django.contrib.auth.models import User


class OrdinaryUser(User, models.Model):
    MAIL = "M"
    FEMAIL = "F"
    GENDER_CHOICES = (
        (MAIL, 'Mail'),
        (FEMAIL, 'Femail')
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=MAIL)
    age = models.PositiveSmallIntegerField(verbose_name='Возраст', blank=True, null=True)
