from django.db import models

# Create your models here.
class Mensaje(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    class Meta:
        ordering = ["id"]
        verbose_name = "Mensaje"
        verbose_name_plural = "Mensajes"

    def __str__(self):
        return self.message