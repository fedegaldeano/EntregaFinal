# pages/views.py
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Page

# (Mantenemos Home y About como TemplateView si querés usarlas más adelante)
class HomeView(TemplateView):
    template_name = 'pages/home.html'

class AboutView(TemplateView):
    template_name = 'pages/about.html'

class PageListView(ListView):
    model = Page
    template_name = 'pages/page_list.html'      # templates/pages/page_list.html
    context_object_name = 'pages'               # en el template usamos 'pages'

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            # búsqueda por título o subtítulo
            return qs.filter(titulo__icontains=q) | qs.filter(subtitulo__icontains=q)
        return qs

class PageDetailView(DetailView):
    model = Page
    template_name = 'pages/page_detail.html'    # templates/pages/page_detail.html

class PageCreateView(LoginRequiredMixin, CreateView):
    model = Page
    fields = ['titulo', 'subtitulo', 'contenido', 'imagen']
    template_name = 'pages/page_form.html'      # templates/pages/page_form.html
    success_url = reverse_lazy('page_list')

    def form_valid(self, form):
        messages.success(self.request, 'Página creada con éxito.')
        return super().form_valid(form)

class PageUpdateView(LoginRequiredMixin, UpdateView):
    model = Page
    fields = ['titulo', 'subtitulo', 'contenido', 'imagen']
    template_name = 'pages/page_form.html'

    def get_success_url(self):
        messages.success(self.request, 'Página actualizada.')
        return reverse_lazy('page_detail', kwargs={'pk': self.object.pk})

class PageDeleteView(LoginRequiredMixin, DeleteView):
    model = Page
    template_name = 'pages/page_confirm_delete.html'
    success_url = reverse_lazy('page_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Página eliminada.')
        return super().delete(request, *args, **kwargs)
