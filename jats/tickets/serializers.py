from rest_framework import serializers

from .models import Ticket, TicketList


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = (
            'id', 'complete', 'creator', 'assigned_to',
            'title', 'due_date', 'notes', 'ticket_list')


class TicketListSerializer(serializers.ModelSerializer):
    tickets = TicketSerializer(many=True, read_only=True)

    class Meta:
        model = TicketList
        fields = ('id', 'name', 'creator', 'tickets',)
