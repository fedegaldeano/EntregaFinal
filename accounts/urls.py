from django.urls import path
from django.contrib.auth import views as auth_views
from .views import SignUpView, profile_view, profile_edit, MyPasswordChangeView

urlpatterns = [
    path('login/',  auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),

    path('profile/', profile_view, name='profile'),
    path('profile/edit/', profile_edit, name='profile_edit'),
    path('password/change/', MyPasswordChangeView.as_view(), name='password_change'),
]
