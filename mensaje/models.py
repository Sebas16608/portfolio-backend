from django.db import models

# Create your models here.
class Mensaje(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.EmailField()
    mensaje = models.TextField()
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Mensaje"
        verbose_name_plural = "Mensajes"

    def __str__(self):
        return f"Mensaje de {self.nombre}"