from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    remitente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensajes_enviados')
    destinatario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensajes_recibidos')
    contenido = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"De {self.remitente} para {self.destinatario} ({self.fecha_envio:%Y-%m-%d %H:%M})"
