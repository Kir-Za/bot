from django.db import models
from django.contrib.auth.models import User


class OrdinaryUser(User, models.Model):
    GENDER = (
        ('M', 'Mail'),
        ('F', 'Femail'),
    )
    gender = models.CharField(verbose_name='Пол', max_length=1, default='M', choices=GENDER)
    age = models.PositiveSmallIntegerField(verbose_name='Возраст', blank=True, null=True)
