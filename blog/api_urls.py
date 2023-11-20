from django.urls import path, include
from .apis import *

urlpatterns = [
    path("hello/", HelloWorldAPI.as_view()),
]