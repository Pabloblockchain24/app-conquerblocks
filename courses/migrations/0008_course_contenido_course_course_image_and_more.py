# Generated by Django 5.1.4 on 2025-02-16 18:05

import django.utils.timezone
import thumbnails.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_remove_course_contenido_remove_course_course_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='contenido',
            field=models.FileField(blank=True, null=True, upload_to='uploads/', verbose_name='Temario'),
        ),
        migrations.AddField(
            model_name='course',
            name='course_image',
            field=thumbnails.fields.ImageField(blank=True, null=True, upload_to='courses/images/', verbose_name='Imagen del curso'),
        ),
        migrations.AddField(
            model_name='course',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de creacion'),
        ),
    ]
