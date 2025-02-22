from django.urls import path 
# from .views import courses_list, course_details, add_course, Cursos_ListView, Cursos_DetailView, CourseFormView, CourseCreateView, CourseUpdateView, CourseDeleteView
from .views import CoursesListView, CourseDetailView, CourseCreateView, CourseUpdateView, CourseDeleteView

app_name = 'courses'

urlpatterns = [
    # path('', courses_list, name='courses_list'),
    # path('add_course/', add_course, name='add_course'),
    # path('add_course_ccbv/', CourseFormView.as_view(), name='add_course_ccbv'),
    # path('<int:id>/', course_details, name='course_details'),
    # path('lista/', Cursos_ListView.as_view(), name='courses_list'),
    # path('lista/<int:pk>/', Cursos_DetailView.as_view(), name='course_detailccbv'),
    # path('add_course_create_view/', CourseCreateView.as_view(), name='add_course_create_view'),
    # path('update_view/<int:pk>/', CourseUpdateView.as_view(), name='update_view'),
    # path('delete_view/<int:pk>/', CourseDeleteView.as_view(), name='delete_view'),

    path('', CoursesListView.as_view(), name='courses_list'),
    path('<int:pk>/', CourseDetailView.as_view(), name='course_details'),
    path('add/', CourseCreateView.as_view(), name='course_create'),
    path('update/<int:pk>/', CourseUpdateView.as_view(), name='update_course'),
    path('delete/<int:pk>/', CourseDeleteView.as_view(), name='delete_course'),

]

