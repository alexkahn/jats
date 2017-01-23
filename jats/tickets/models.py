from django.conf import settings
from django.db import models


class TicketGroup(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=70, blank=False)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return "{} - {}".format(self.name, self.creator)


class Ticket(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    complete = models.BooleanField(default=False, null=False)
    ticket_group = models.ForeignKey('TicketGroup')
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='created_tickets')
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='assigned_tickets',
        default=None, null=True)
    title = models.CharField(max_length=140, blank=False)
    due_date = models.DateTimeField(blank=True, null=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return '{created} - {creator}: {title}'.format(
            created=self.created, creator=self.creator, title=self.title)
