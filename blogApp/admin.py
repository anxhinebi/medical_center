from django.contrib import admin
from .models import News, Discount, Job

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'image', 'content', 'writer')
    search_fields = ('title', 'content', 'writer')

@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('title', 'from_date', 'to_date', 'created_at', 'updated_at', 'image', 'content')
    search_fields = ('title', 'content')

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'content')
    search_fields = ('title', 'content')
