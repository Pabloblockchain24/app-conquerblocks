from datetime import datetime
from blogs.models import Post
from courses.models import Course

def get_current_year(request):
    current_year = datetime.now().year
    return {
        'current_year': current_year
    }

def get_statistics(request):
    total_posts = Post.objects.count()
    total_courses = Course.objects.count()
    return {
        'total_posts': total_posts,
        'total_courses': total_courses
    }
