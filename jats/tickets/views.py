from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Ticket, TicketList
from .serializers import TicketSerializer, TicketListSerializer


class TicketViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()

    def get_queryset(self):
        return Ticket.objects.filter(creator=self.request.user.id)


class TicketListViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = TicketListSerializer
    queryset = TicketList.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(creator=self.request.user.id)
