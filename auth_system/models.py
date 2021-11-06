from django.conf import settings
from django.db import models

from auth_system.choices import GenderChoices
from auth_system.mixins import AutoHistoryMixin


class User2(AutoHistoryMixin):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT, verbose_name='Django User',
    )
    first_name = models.CharField(max_length=70, null=True, blank=True)
    surname = models.CharField(max_length=70, null=True, blank=True)
    second_name = models.CharField(max_length=70, null=True, blank=True)
    gender = models.CharField(
        max_length=20, choices=GenderChoices.CHOICES, default=GenderChoices.MALE,
    )

    class Meta:
        verbose_name = 'Custom User'
        verbose_name_plural = 'Custom Users'

    def __str__(self):
        return f'{self.surname} {self.first_name} {self.second_name}'
