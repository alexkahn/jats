from rest_framework import serializers

from .models import Ticket


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = (
            'complete', 'ticket_group', 'creator', 'assigned_to', 'title',
            'due_date', 'notes',)
