from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm  # (puede quedar, no molesta)
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView
from .forms import UserUpdateForm, ProfileUpdateForm  # si ya lo tenías en paso 9

class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('login')

@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html')

@login_required
def profile_edit(request):
    uform = UserUpdateForm(instance=request.user)
    pform = ProfileUpdateForm(instance=getattr(request.user, 'profile', None))
    if request.method == 'POST':
        uform = UserUpdateForm(request.POST, instance=request.user)
        pform = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if uform.is_valid() and pform.is_valid():
            uform.save()
            pform.save()
            messages.success(request, 'Perfil actualizado con éxito.')
            return redirect('profile')
    return render(request, 'accounts/profile_edit.html', {'uform': uform, 'pform': pform})

class MyPasswordChangeView(PasswordChangeView):
    template_name = 'accounts/password_change.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        messages.success(self.request, 'Contraseña cambiada con éxito.')
        return super().form_valid(form)
