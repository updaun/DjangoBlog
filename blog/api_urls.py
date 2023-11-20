from django.urls import path, include
from .apis import *

# http://127.0.0.1:8000/blog/
urlpatterns = [
    # http://127.0.0.1:8000/api/blog/
    path("", BlogAPI.as_view()),
    # http://127.0.0.1:8000/api/blog/<int:pk>/
    path("<int:pk>/", BlogDetailAPI.as_view()),
    # http://127.0.0.1:8000/api/blog/hello/
    path("hello/", HelloWorldAPI.as_view()),
]