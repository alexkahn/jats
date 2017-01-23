from rest_framework import viewsets

from .models import Ticket
from .serializers import TicketSerializer


class TicketViewSet(viewsets.ModelViewSet):
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()

    def get_queryset(self):
        return Ticket.objects.filter(creator=self.request.user.id)
