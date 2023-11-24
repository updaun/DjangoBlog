from django.shortcuts import render
from django.http.response import HttpResponse
import random
from .models import Blog
from django.views import View
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.mixins import LoginRequiredMixin


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
        try:
            blog = Blog.objects.get(id=blogid)
        except Blog.DoesNotExist:
            return HttpResponse("<h1>Blog not found</h1>")
        return render(request, "blog/detail.html", {"owner":blog.user})
    

class BlogCreateView(View):
    def get(self, request):
        return render(request, "blog/create.html")
    

class BlogUpdateView(View):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            blog = Blog.objects.get(id=pk)
            if blog.user != request.user:
                return HttpResponse("<h1>Permission Denied</h1>")
        except Blog.DoesNotExist:
            return HttpResponse("<h1>Blog not found</h1>")
        return render(request, "blog/update.html")
    

class MyBlogView(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, "blog/myblog.html")