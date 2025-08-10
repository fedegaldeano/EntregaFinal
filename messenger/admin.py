from django.contrib import admin
from .models import Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('remitente', 'destinatario', 'fecha_envio')
    search_fields = ('remitente__username', 'destinatario__username', 'contenido')
