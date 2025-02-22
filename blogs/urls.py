from django.urls import path 

from .views import BlogsListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

app_name = 'blogs'

urlpatterns = [
    path('', BlogsListView.as_view(), name='blogs_list'),
    path('<int:pk>/', BlogDetailView.as_view(), name='blog_details'),
    path('add/', BlogCreateView.as_view(), name='blog_create'),
    path('update/<int:pk>/', BlogUpdateView.as_view(), name='update_blog'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete_blog'),
] 