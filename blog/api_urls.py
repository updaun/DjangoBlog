from django.urls import path, include
from .apis import *

urlpatterns = [
    path("hello/", HelloWorldAPI.as_view()),
    path("", BlogAPI.as_view()),
    path("<int:pk>/", BlogDetailAPI.as_view()),
]