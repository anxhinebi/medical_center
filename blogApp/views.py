from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import News, Discount, Job
from django.core.paginator import Paginator
from heallthApp.models import Reservation, Service
from django.db.models import Q

def home(request):
    return render(request, "home.html")

def blog_home(request):
    services = Service.objects.all()
    news = News.objects.all().order_by('-created_at')
    discounts = Discount.objects.all()
    jobs = Job.objects.all()
    writers = News.objects.values_list('writer', flat=True).distinct()
    recent_posts = news[:5]
   
    paginator = Paginator(news, 3)
    page_number = request.GET.get('page')
    news = paginator.get_page(page_number)
    context = {
        'news': news,
        'discounts': discounts,
        'jobs': jobs,
        'writers': writers,
        'recent_posts': recent_posts,
        'services': services
    }
    return render(request, 'blogHome.html', context)


def blog_search(request):
    services = Service.objects.all()
    query = request.GET.get('q', '')
    results = News.objects.filter(Q(title__icontains=query) | Q(content__icontains=query)
    ) if query else []
    return render(request, 'blog_search_results.html', {'results': results, 'query': query, 'services': services})

def blog_post(request, pk):
    services = Service.objects.all()
    post = get_object_or_404(News, pk=pk)
    return render(request, 'blogPosts.html', {'post': post, 'services': services})

def blog_discount(request, pk):
    services = Service.objects.all()
    discount = get_object_or_404(Discount, pk=pk)
    return render(request, 'blogDiscount.html', {'discount': discount, 'services': services})

def blog_job(request, pk):
    services = Service.objects.all()
    job = get_object_or_404(Job, pk=pk)
    return render(request, 'blogJob.html', {'job': job, 'services': services})