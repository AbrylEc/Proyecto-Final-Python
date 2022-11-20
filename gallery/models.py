from django.db import models

# Create your models here.
# Los modelos siempre se colocan en singular


class Gallery(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    image = models.ImageField(verbose_name="Imagen", upload_to="gallery")
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "galería"
        verbose_name_plural = "galerías"
        ordering = ['-created']

    def __str__(self):
        return self.title
