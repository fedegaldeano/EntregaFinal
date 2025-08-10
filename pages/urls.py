# pages/urls.py
from django.urls import path
from .views import (
    HomeView, AboutView,
    PageListView, PageDetailView, PageCreateView, PageUpdateView, PageDeleteView
)

urlpatterns = [
    path('', PageListView.as_view(), name='page_list'),                  # /listado/
    path('pages/', PageListView.as_view(), name='page_list_alias'),      # /pages/
    path('about/', AboutView.as_view(), name='about'),                   # /about/
    path('home/', HomeView.as_view(), name='home'),                      # /home/
    path('<int:pk>/', PageDetailView.as_view(), name='page_detail'),     # /<id>/
    path('create/', PageCreateView.as_view(), name='page_create'),       # /create/
    path('<int:pk>/edit/', PageUpdateView.as_view(), name='page_update'),# /<id>/edit/
    path('<int:pk>/delete/', PageDeleteView.as_view(), name='page_delete'),# /<id>/delete/
]
