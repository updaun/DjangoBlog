from django.urls import path, include
from .apis import *

# http://127.0.0.1:8000/api/blog/
urlpatterns = [
    path("", BlogAPI.as_view()),
    path("<int:pk>/", BlogDetailAPI.as_view()),
    # http://127.0.0.1:8000/api/blog/hello/
    path("hello/", HelloWorldAPI.as_view()),
]