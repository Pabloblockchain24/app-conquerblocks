from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
class Post(models.Model):

    created_by = models.ForeignKey(
        User, 
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL
    )

    title = models.CharField(
        verbose_name='Titulo del blog',
        max_length=200
        )
    content = models.TextField(
        verbose_name='Contenido del blog'
    )
    author = models.CharField(
        verbose_name='Autor del blog',
        max_length=100
        )
    created_at = models.DateTimeField(
        verbose_name='Fecha de creacion',
        default=timezone.now
        )

    def __str__(self):
        return self.title