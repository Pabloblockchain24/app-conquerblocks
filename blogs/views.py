from .models import Post
from django.contrib import messages
from django.utils.translation import gettext as _

from django.views.generic.list import ListView
class BlogsListView(ListView):
    model = Post
    template_name = 'blogs/blogs_list.html'
    context_object_name = 'blogs'


from django.views.generic.detail import DetailView
class BlogDetailView(DetailView):
    model = Post
    template_name = 'blogs/blog_detail.html'
    context_object_name = 'blog'

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.views.generic.edit import CreateView
@method_decorator(login_required, name='dispatch')
class BlogCreateView(CreateView):
    model = Post
    fields = ['title', 'content', 'author']
    template_name = 'blogs/blog_create.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        messages.success(self.request, _('¡El blog se ha creado con éxito!'))
        return super().form_valid(form)
    
from django.views.generic.edit import UpdateView
@method_decorator(login_required, name='dispatch')
class BlogUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content', 'author']
    template_name = 'blogs/blog_update.html'
    success_url = '/'

from .decorators import user_can_delete_post
from django.views.generic.edit import DeleteView
@method_decorator(user_can_delete_post, name='dispatch')
class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'blogs/blog_delete.html'
    success_url = '/'