from django.contrib import admin

# Register your models here.
from .models import Contact

@admin.register(Contact)
class ContactResource(admin.ModelAdmin):
        model = Contact
        list_display = ('name', 'email', 'create_at')

