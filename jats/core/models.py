from django.conf import settings
from django.contrib.postgres.fields import JSONField
from django.db import models


def default_settings():
    return {
        'tickets': {
            'reminder': 'in an hour',
            'due_date': 'today'
        }
    }


class Settings(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    data = JSONField(default=default_settings)