from django.contrib.auth.models import User
from django.db import models


class User2(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    surname = models.CharField(max_length=30, null=True, blank=True, verbose_name='Фамилия')
    firstname = models.CharField(max_length=30, null=True, blank=True, verbose_name='Имя')
    second_name = models.CharField(max_length=30, null=True, blank=True, verbose_name='Отчество')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.surname} {self.firstname} {self.second_name}'
