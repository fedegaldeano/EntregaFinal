from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Message

class MessageListView(LoginRequiredMixin, ListView):
    model = Message
    template_name = 'messenger/message_list.html'

    def get_queryset(self):
        # Inbox: solo los recibidos por el usuario logueado
        return Message.objects.filter(destinatario=self.request.user).order_by('-fecha_envio')

class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    fields = ['destinatario', 'contenido']
    template_name = 'messenger/message_form.html'
    success_url = reverse_lazy('inbox')

    def form_valid(self, form):
        form.instance.remitente = self.request.user
        return super().form_valid(form)
