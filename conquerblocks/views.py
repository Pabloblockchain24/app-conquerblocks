from django.utils import translation
from django.http import HttpResponseRedirect
from django.views import View


class SetLanguageView(View):
    def post(self, request, *args, **kwargs):
        language = request.POST.get('language', None)
        if language:
            translation.activate(language)
            # request.session[translation.LANGUAGE_SESSION_KEY] = language

        next_url = request.POST.get('next', '/')
        return HttpResponseRedirect(next_url)        
    