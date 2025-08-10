from django.urls import path
from .views import MessageListView, MessageCreateView

urlpatterns = [
    path('', MessageListView.as_view(), name='inbox'),          # /messenger/
    path('nuevo/', MessageCreateView.as_view(), name='enviar'), # /messenger/nuevo/
]
