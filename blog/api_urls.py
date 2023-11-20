from django.urls import path, include
from .apis import *


# http://127.0.0.1:8000/api/blog/
urlpatterns = [
    # http://127.0.0.1:8000/api/blog/
    path("",BlogAPI.as_view()),

    # http://127.0.0.1:8000/api/blog/<int:pk>/
    path("<int:pk>/",BlogDetailAPI.as_view()),

    # http://127.0.0.1:8000/api/blog/hello/
    path("hello/",HelloWorldAPI.as_view()),

]

# get만 redirect (301)해서 "/"없이도 보여주지만, 나머지는 "/"가 필수다.
# 다른 메소드는 "/"에 민감하다
# 더 restful 하다고는 하는데,"/"는 회사마다 다르다.