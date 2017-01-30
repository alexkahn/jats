from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer


class Home(TemplateView):
    template_name = 'index.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return App.as_view()(request, *args, **kwargs)
        return super(Home, self).dispatch(request, *args, **kwargs)


class App(LoginRequiredMixin, TemplateView):
    template_name = 'app.html'


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    def list(self, *args, **kwargs):
        queryset = self.get_queryset()
        user = get_object_or_404(queryset, pk=self.request.user.id)
        serializer = self.get_serializer(instance=user)
        return Response(serializer.data)