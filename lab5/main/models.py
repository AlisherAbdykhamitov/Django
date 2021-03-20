import datetime

from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Todo(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['id', 'name']
        verbose_name = 'Список'
        verbose_name_plural = 'Списки'




class Task(models.Model):
    name = models.CharField(max_length=240)
    created = models.DateField(auto_now_add=True)
    due = models.DateField(default=(datetime.datetime.now() + datetime.timedelta(days=2)).date())
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    completed = models.BooleanField(default=False)
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE, default = models.CASCADE, null=True, blank=True,
                             related_name='tasks')

    class Meta:
        ordering = ['id', 'name']
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

