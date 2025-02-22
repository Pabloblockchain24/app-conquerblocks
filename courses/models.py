from django.db import models
from django.utils import timezone
from thumbnails.fields import ImageField
from ckeditor.fields import RichTextField

class Course(models.Model):
    title = models.CharField(
        verbose_name='Titulo del curso',
        max_length=200,
        )
    content = RichTextField(
        verbose_name='Contenido del curso',
        null=True,
        blank=True,   
    )
    call_link = models.URLField(
        verbose_name='Enlace de llamada',
        null=True,
        blank=True,
        )
    created_at = models.DateTimeField(
        verbose_name='Fecha de creacion',
        default=timezone.now,
        )
    
    contenido = models.FileField(
        verbose_name="Temario",
        upload_to='uploads/',
        null=True,
        blank=True,
    )

    course_image = ImageField(
        verbose_name = "Imagen del curso",
        upload_to='courses/images/',
        null=True,        
        blank=True,
    )
    
    def __str__(self):
        return self.title