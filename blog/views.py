import random
from django.http import HttpResponse
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
        try:
            blog = Blog.objects.get(pk=pk)
        except Blog.DoesNotExist:
            return HttpResponse("<h1>Blog not found</h1>")
        return render(request, 'blog/detail.html', {"owner": blog.user})     
    

class BlogCreateView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'blog/create.html')
    

class BlogUpdateView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'blog/update.html')
        