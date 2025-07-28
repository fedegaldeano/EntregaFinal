from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Mensaje

class BandejaEntradaView(LoginRequiredMixin, ListView):
    model = Mensaje
    template_name = 'messenger/bandeja_entrada.html'

    def get_queryset(self):
        return Mensaje.objects.filter(receptor=self.request.user).order_by('-fecha')
