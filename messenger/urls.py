from django.urls import path
from .views import BandejaEntradaView

urlpatterns = [
    path('inbox/', BandejaEntradaView.as_view(), name='inbox'),
]
