from django.db import models
from django.utils import timezone
# Create your models here.

class Contact(models.Model):
    name = models.CharField(
        verbose_name='Nombre',
        max_length=200
    )
    email = models.EmailField(
        verbose_name='Email'
    )
    message = models.TextField(
        verbose_name='Mensaje que ha dejado en la web'
    )
    create_at = models.DateTimeField(
        verbose_name='Fecha de creacion',
        default=timezone.now
    )

    def __str__(self):
        return self.name