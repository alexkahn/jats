from django.db import models
from django.conf import settings


class Administrator(models.Model):
    organization = models.ForeignKey('organizations.Organization')
    user = models.ForeignKey(settings.AUTH_USER_MODEL)


class Organization(models.Model):
    name = models.CharField(max_length=140, blank=False, null=False)
    administrators = models.ManyToManyField(
        settings.AUTH_USER_MODEL, through=Administrator)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL)
    deleted = models.BooleanField(default=False)
