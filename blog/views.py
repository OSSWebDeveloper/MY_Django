from django.shortcuts import render
from .models import Post
from django.utils import timezone

# Create your views here.

def index(request):
    news = Post.objects.order_by('-date')[:3]
    return render(request, "blog/index.html"), {'news':news}

def blog(request):
    news = Post.objects.all()
    return render(request, 'blog/index.html') , {'news':news}


from django.db.models import Q

def search_result(request):
    query = request.GET.get('search')
    search_obj = Post.objects.filter(
        Q(title__icontains=query) |Q(summary__icontains=query)
    )
    return render(request, 'blog/search.html',
{'search_obj':search_obj, 'query':query})
