from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class Home(TemplateView):
    template_name = 'index.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return App.as_view()(request, *args, **kwargs)
        return super(Home, self).dispatch(request, *args, **kwargs)


class App(LoginRequiredMixin, TemplateView):
    template_name = 'app.html'
