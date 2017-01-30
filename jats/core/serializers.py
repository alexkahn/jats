from django.contrib.auth import get_user_model

from rest_framework import serializers

from jats.tickets.serializers import TicketListSerializer


class UserSerializer(serializers.ModelSerializer):
    ticketlist_set = TicketListSerializer(many=True, read_only=True)

    class Meta:
        model = get_user_model()
        fields = (
            'id', 'ticketlist_set')
