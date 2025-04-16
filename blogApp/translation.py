from modeltranslation.translator import register, TranslationOptions
from .models import News, Discount, Job

@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'content')

@register(Discount)
class DiscountTranslationOptions(TranslationOptions):
    fields = ('title', 'content')
    
@register(Job)
class JobTranslationOptions(TranslationOptions):
    fields = ('title', 'content')