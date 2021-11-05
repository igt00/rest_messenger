from django.contrib.auth.models import User
from django.db import models


class User2(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, verbose_name='Django User')
    first_name = models.CharField(max_length=70, null=True, blank=True)
    surname = models.CharField(max_length=70, null=True, blank=True)
    second_name = models.CharField(max_length=70, null=True, blank=True)

    class Meta:
        verbose_name = 'Custom User'
        verbose_name_plural = 'Custom Users'

    def __str__(self):
        return f'{self.surname} {self.first_name} {self.second_name}'
