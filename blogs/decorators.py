from .models import Post
from django.http import Http404
from django.core.exceptions import PermissionDenied

def user_can_delete_post(function):
    def wrapper(request, *args, **kwargs):
        try:
            post = Post.objects.get(pk=kwargs['pk'])
        except Post.DoesNotExist:
            raise Http404
        
        if request.user == post.created_by:
            return function(request, *args, **kwargs)
        raise PermissionDenied

    return wrapper