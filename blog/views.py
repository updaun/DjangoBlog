import random
from django.shortcuts import render
from django.views.generic import ListView
from django.views import View
from .models import Blog

def blog_list(request, *args, **kwargs):
    context = {}
    context['number'] = random.randint(1 ,1000)
    if request.method == 'GET':
        context['blogs'] = Blog.objects.all()

    return render(request, 'blog/blog_list.html', context)


class BlogListView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        context['number'] = random.randint(1 ,1000)
        context['blogs'] = Blog.objects.all()
        return render(request, 'blog/blog_list.html', context)
    
class BlogDetailView(View):
    def get(self, request, pk):
        
        context = {}
        context['blogs'] = [Blog.objects.get(id=pk)]
        return render(request, 'blog/blog_list.html', context)     