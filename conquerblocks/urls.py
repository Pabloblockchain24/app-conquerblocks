from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf.urls.i18n import i18n_patterns


urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')), # this line add a view 'set_language' by default to my proyect 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  + debug_toolbar_urls()

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='core')),
    path('courses/', include('courses.urls', namespace='courses')),
    path('blogs/', include('blogs.urls', namespace='blogs'))
) 

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        path('rosetta/', include('rosetta.urls')),
    ]
