from django.db import models
from django.contrib.auth.models import User


class OrdinaryUser(User, models.Model):
    gender = models.BooleanField(verbose_name='Пол (м. -1)')
    age = models.PositiveSmallIntegerField(verbose_name='Возраст')
    '''
    favorite_news_theme = models.ManyToManyField(
        'newsblog.Themes',
        related_name='users_themes',
        verbose_name='Избранное'
    )
    users_notes = models.ForeignKey('notes.Record', related_name='my_note', verbose_name='Заметки пользователя')
    users_sprint = models.OneToOneField('todolist.Sprint', related_name='my_work', verbose_name='Список дел')
    '''


