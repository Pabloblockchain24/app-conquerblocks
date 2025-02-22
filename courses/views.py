# from django.shortcuts import render, redirect
from .models import Course
# from django.contrib.auth.decorators import login_required
# from django.urls import reverse
# cursos = Course.objects.all() 

#Vistas generales de la app
# @login_required
# def courses_list(req):
#     context = {
#     'courses': cursos,
#     'title': 'Listado de cursos'   
#     }
#     return render(req, 'courses/courses_list.html', context)

# def course_details(req, id):
#     try:
#         context = {
#             "course": cursos[id-1],
#             "title": 'Este es el curso'
#         }    
#     except IndexError:
#         context = {
#             "course": None,
#             "title": f'Curso con id {id} no existe.',
#         }
#     return render(req, 'courses/course_detail.html', context)


# from .forms import CourseForm
# def add_course(req):
#     if req.POST:
#         form = CourseForm(req.POST)
#         if form.is_valid():
#             course = Course.objects.create(
#                 title = form.cleaned_data['title'],
#                 content = form.cleaned_data['content'],
#                 call_link = form.cleaned_data['call_link'],
#                 created_at = form.cleaned_data['created_at'],
#                 contenido = form.cleaned_data['contenido'],
#                 course_image = form.cleaned_data['course_image']
#             )
#             return redirect(reverse('courses:course_details', args=[course.id-1]))
#     else:
#         form = CourseForm()    

#     context = {
#         'form': form
#     }      
       
#     return render(req, 'courses/add_course.html', context)

#from django.views.generic.edit import FormView

# class CourseFormView(FormView):
#     template_name = 'courses/add_course_ccbv.html'
#     form_class = CourseForm
#     success_url = '/'

#     def form_valid(self, form):
#         course = Course.objects.create(
#                 title = form.cleaned_data['title'],
#                 content = form.cleaned_data['content'],
#                 call_link = form.cleaned_data['call_link'],
#                 created_at = form.cleaned_data['created_at'],
#                 contenido = form.cleaned_data['contenido'],
#                 course_image = form.cleaned_data['course_image']
#             )
#         return redirect(reverse('courses:course_details', args=[course.id-1]))


from django.views.generic.list import ListView
class CoursesListView(ListView):
    model = Course
    template_name = 'courses/courses_list.html'
    context_object_name = 'courses'



from django.views.generic.detail import DetailView
class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/course_detail.html'
    context_object_name = 'course'


from django.views.generic.edit import CreateView
class CourseCreateView(CreateView):
    model = Course
    fields = ['title', 'content', 'call_link', 'created_at', 'contenido', 'course_image']
    template_name = 'courses/course_create.html'
    success_url = '/'

from django.views.generic.edit import UpdateView
class CourseUpdateView(UpdateView):
    model = Course
    fields = ['title', 'content', 'call_link', 'created_at', 'contenido', 'course_image']
    template_name = 'courses/course_update.html'
    success_url = '/'

from django.views.generic.edit import DeleteView
class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'courses/course_delete.html'
    success_url = '/'
