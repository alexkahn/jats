from rest_framework import serializers

from .models import Ticket, TicketList


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = (
            'id', 'complete', 'ticket_list', 'creator', 'assigned_to',
            'title', 'due_date', 'notes',)


class TicketListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketList
        fields = ('name', 'creator',)
