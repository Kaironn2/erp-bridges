from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import TemplateView


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'core/home.html'


class CustomLoginView(LoginView):
    template_name = 'core/login.html'
    success_url = reverse_lazy('home')


class TestView(TemplateView):
    template_name = 'core/test.html'
