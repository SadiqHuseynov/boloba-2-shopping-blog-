from modeltranslation.translator import translator, TranslationOptions, register

from .models import Blogs

@register(Blogs)
class BlogTranslation(TranslationOptions):
    fields = ('title','description',)