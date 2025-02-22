from modeltranslation.translator import translator, TranslationOptions
from .models import Post

class BlogTranslationOptions(TranslationOptions):
    fields = ('title', 'content', 'author', 'created_by')

translator.register(Post, BlogTranslationOptions)