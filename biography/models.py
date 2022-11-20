from django.db import models
from django.utils.timezone import now
# Importar modelo user

# Create your models here.
# Siempre el modelo en singular -> Category


class Biography(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    image = models.ImageField(verbose_name="Imagen", upload_to="biography")
    content = models.TextField(verbose_name="Contenido")
    published = models.CharField(max_length=200, verbose_name="Fecha")
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "evento"
        verbose_name_plural = "eventos"
        ordering = ['created']

    def __str__(self):
        return self.title
