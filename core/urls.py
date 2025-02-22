from django.contrib import admin
from django.urls import path

from .views import home_view, login_view, register_view, about_us, contact_view, logout_view, Prueba_view, Prueba_TemplateView     

app_name = 'core'

urlpatterns = [
    path('', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('about-us/', about_us, name='about_us'),
    path('contact-us/', contact_view, name='contact_us'),
    path('prueba/', Prueba_view.as_view() , name='prueba'),
    path('template_view/', Prueba_TemplateView.as_view() , name='template_view'),
]



