# Generated by Django 5.1.4 on 2025-02-16 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_alter_course_call_link_alter_course_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='contenido',
        ),
        migrations.RemoveField(
            model_name='course',
            name='course_image',
        ),
        migrations.RemoveField(
            model_name='course',
            name='created_at',
        ),
    ]
