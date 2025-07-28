from django.urls import path
from .views import (
    PageListView,
    PageDetailView,
    PageCreateView,
    PageUpdateView,
    PageDeleteView,
)

urlpatterns = [
    path('', PageListView.as_view(), name='page_list'),
    path('<int:pk>/', PageDetailView.as_view(), name='page_detail'),
    path('crear/', PageCreateView.as_view(), name='page_create'),
    path('editar/<int:pk>/', PageUpdateView.as_view(), name='page_update'),
    path('borrar/<int:pk>/', PageDeleteView.as_view(), name='page_delete'),
]
