from django.db import models
from ckeditor.fields import RichTextField

class Page(models.Model):
    titulo = models.CharField(max_length=200)         # CharField 1
    subtitulo = models.CharField(max_length=250)      # CharField 2
    contenido = RichTextField()                       # Texto enriquecido (ckeditor)
    imagen = models.ImageField(upload_to='pages/', blank=True, null=True)  # Imagen
    fecha_publicacion = models.DateField(auto_now_add=True)                # Fecha

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.titulo
