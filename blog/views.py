from django.shortcuts import render
from django.http.response import HttpResponse
import random
from .models import Blog
from django.views import View
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.mixins import LoginRequiredMixin


# FBV - Function Based View
def blog_list(request):
    random_number = random.randint(1,10000)

    blog_list = Blog.objects.all()  # queryset (list)of Blog objects

    return render(request,"blog_list.html",{"number": random_number,"blogs":blog_list})
    # return HttpResponse("blog_list")


# CBV - Class Based View : 웹 프레임워크의 기능들(Django는 Web을 위한 도구!)을 활용할 수 있다, 코드 가시성이 좋아진다.
class BlogListView(View):
    
    # 클래스 안에는 "함수"가 아니라 "메소드"라고 한다.
    # 메소드이기 때문에, 함수와는 달리 self를 넣어줘야 한다.
    # get 메소드를 사용했기에, 다른 사람들로 하여금 힌트를 줄 수 있어서 가독성이 좋다.
    def get(self,request):
        random_number = random.randint(1,10000)
        blog_list = Blog.objects.all()  # queryset (list)of Blog objects
        return render(request,"blog_list.html",{"number": random_number,"blogs":blog_list})
    

class BlogDetailView(View):

    def get(self,request,blogid):

        try:
            blog = Blog.objects.get(id=blogid)
        except Blog.DoesNotExist:
            return HttpResponse("<h1>Blog not found</h1>")

        return render(request,"blog/detail.html", {"owner":blog.user})

        # blog = Blog.objects.get(id=blogid)
        # return render(request,"blog_list.html",{"blogs":[blog]})


class BlogCreateView(View):
    def get(self,request):
        return render(request,"blog/create.html")


class BlogUpdateView(View):
    permission_classes = [IsAuthenticated]

    def get(self,request,pk):
        try:
            blog = Blog.objects.get(id=pk)
            if blog.user != request.user:
                return HttpResponse("<h1>Permission Denied</h1>")
        except Blog.DoesNotExist:
            return HttpResponse("<h1>Blog not found</h1>")
        return render(request,"blog/update.html")
    

# 로그인을 해야지만 접근할 수 있도록 LoginRequiredMixin을 상속
class MyBlogView(LoginRequiredMixin,View):

    def get(self,request):
        return render(request,"blog/myblog.html")