from django.db import models


class AutoHistoryMixin(models.Model):
    dt_created = models.DateTimeField(auto_now_add=True, null=True)
    dt_updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True
