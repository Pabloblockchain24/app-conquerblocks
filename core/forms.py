from django import forms
from django.utils.translation import gettext_lazy as _

class ContactForm(forms.Form):
    name = forms.CharField(
        label=_("Nombre"),
        max_length=100
    )
    email = forms.EmailField(
        label=_("Email")
    )

    def clean_name(self):
        nombre = self.cleaned_data['name']
        if len(nombre) < 5:
            raise forms.ValidationError(_("El nombre debe tener al menos 5 caracteres"))
        return nombre

class LoginForm(forms.Form):
    username = forms.CharField(
        label=_("Nombre de usuario"),
        max_length=100
    )
    password = forms.CharField(
        label=_("Contraseña"),
        widget=forms.PasswordInput()
    )


from django.contrib.auth.password_validation import validate_password

class UserRegisterForm(forms.Form):
    username = forms.CharField(label="Nombre de usuario", max_length=140)
    first_name = forms.CharField(label="Nombre",max_length=140)
    last_name = forms.CharField(label="Apellido",max_length=140)
    email = forms.EmailField(label="Email",max_length=140) 
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Confirmar contraseña",widget=forms.PasswordInput())

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 != password2 and password1 != '' :
            raise forms.ValidationError("Las contraseñas no coinciden")
        

        if password2 != '':
            validate_password(password2)  

        return password2