from django.shortcuts import render, redirect
from courses.models import Course
from blogs.models import Post
from .forms import ContactForm, LoginForm 
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.models import User


#Vistas generales de la app
def home_view(req):
    context = {
    'courses': Course.objects.all(),
    'blogs': Post.objects.all(),
    }


    return render(req, 'core/home.html', context)

def about_us(req):
    return render(req, 'core/about_us.html')

def login_view(req):
    if req.POST:
        form = LoginForm(req.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(req, user)
                return redirect(reverse('core:home'))
            else:
                context = {
                    'form': form,
                    'error': True,
                    'error_message': 'Usuario no valido'
                }    
                return render(req, 'core/login.html', context)
        else:
            context = {
                'form': form,
                'error': True
                }    
            return render(req, 'core/login.html', context)
    else:
        form = LoginForm()
        context = {
            'form': form
        }      
        return render(req, 'core/login.html', context)

def logout_view(req):
    logout(req)
    return redirect(reverse('core:home'))


from django.core.mail import send_mail
from .models import Contact

def contact_view(req):
    
    if req.POST:
        formulario = ContactForm(req.POST)      

        if formulario.is_valid():
            nombre = formulario.cleaned_data['name']
            email = formulario.cleaned_data['email']
            Contact.objects.create(name=nombre, email=email )
            success  = send_mail(
                "Formulario de contacto de la web",
                nombre,
                "parcepaiva@gmail.com",
                ["pablo.arce.p@mail.pucv.cl"],
                fail_silently=False,
            )

            context = {
                "formulario": formulario,
                "success": success
            }
            return render(req, 'core/contact_us.html', context)
        else:
            context = {
                "formulario": formulario,
                "success": False
            }
            return render(req, 'core/contact_us.html', context)

    formulario = ContactForm()
    context = {
        "form": formulario,
    }

    return render(req, 'core/contact_us.html', context)


from .forms import UserRegisterForm
def register_view(req):
    if req.POST:
        form = UserRegisterForm(req.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            user = User.objects.create_user(username, email, password2)
            if user:
                user.first_name = first_name
                user.last_name = last_name
                user.save()
            context = {
                'msj': 'Usuario creado correctamente'
            }
            return render(req, "core/register.html", context)
        else:
                context = {
                    'form': form,
                    'error': True,
                }    
                return render(req, 'core/register.html', context)
    else:
        form = UserRegisterForm()
        context = {
            'form': form
        }      
        return render(req, 'core/login.html', context )
    


from django.views import View
from django.http import HttpResponse
class Prueba_view(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hola Pablo")
    
from django.views.generic.base import TemplateView

class Prueba_TemplateView(TemplateView):
    template_name = 'core/prueba.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Template View ustando el get_context_data'
        return context
    

class Prueba_TemplateView2(Prueba_TemplateView):
    template_name = 'core/prueba.html'
    

