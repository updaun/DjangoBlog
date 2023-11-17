from django.shortcuts import render
from django.http.response import HttpResponse
import random
from .models import Blog
from django.views import View


def blog_list(request):
    random_number = random.randint(1, 10000)
    blog_list = Blog.objects.all()
    return render(request, "blog_list.html", {"number": random_number, "blogs": blog_list})


class BlogListView(View):
    def get(self, request):
        random_number = random.randint(1, 10000)
        blog_list = Blog.objects.all()
        return render(request, "blog_list.html", {"number": random_number, "blogs": blog_list})
    
class BlogDetailView(View):
    def get(self, request, blogid):
        blog = Blog.objects.get(id=blogid) 
        return render(request, "blog_list.html", {"blogs": [blog]})