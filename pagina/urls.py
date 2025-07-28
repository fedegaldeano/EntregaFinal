from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),  # Esto maneja / y /about/
    path('licitaciones/', include('licitaciones.urls')),  # mové esto a /licitaciones/
    path('accounts/', include('accounts.urls')),
    path('mensajes/', include('messenger.urls')),
]
