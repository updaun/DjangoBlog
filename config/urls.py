"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path("", HomeView.as_view()),
    # http://127.0.0.1:8000/hello/
    path("hello/", helloworld),
    # http://127.0.0.1:8000/hello/json/
    path("hello/json/", helloworld_json),
    # http://127.0.0.1:8000/random/
    path("random/", random_number),
    # http://127.0.0.1:8000/blog/
    path("blog/", include("blog.urls")),
    # http://127.0.0.1:8000/api/blog/
    path("api/blog/", include("blog.api_urls")),
    # http://127.0.0.1:8000/admin/
    path('admin/', admin.site.urls),
]
