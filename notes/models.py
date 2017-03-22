from django.db import models


class MyNote(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название заметки')
    keys = models.CharField(max_length=255, verbose_name='Ключевые слова')
    text_body = models.TextField(verbose_name='Заметка')
    time_add = models.DateTimeField(verbose_name='Время добавления', auto_now=True)
