from django.db import models


class Reminder(models.Model):
    time = models.DateTimeField(verbose_name='Время срабатывания')
    note = models.CharField(max_length=511, verbose_name='Текс напоминания')
    customer = models.ForeignKey('interface.OrdinaryUser', on_delete=models.CASCADE)
    status = models.BooleanField(default=True, verbose_name='Актуальность напоминания')


class ToDoList(models.Model):
    status = models.BooleanField(default=False, verbose_name='Состояние задачи')
    note = models.TextField(verbose_name='Описание задачи')
    time = models.DateTimeField(auto_now=True, verbose_name='Время добавления')
    customer = models.ForeignKey('interface.OrdinaryUser', on_delete=models.CASCADE)


class TimeManage(models.Model):
    start_time = models.TimeField(verbose_name='Start')
    stop_time = models.TimeField(verbose_name='Stop')
    current_day = models.DateField(verbose_name='Рабочий день')
    current_day_time = models.PositiveIntegerField()
    customer = models.ForeignKey('interface.OrdinaryUser', on_delete=models.CASCADE)
