# Generated by Django 5.1.4 on 2025-02-10 16:13

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='create_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de creacion'),
        ),
    ]
