from django.urls import path, include
from .views import *

# http://127.0.0.1:8000/blog/
urlpatterns = [
    # http://127.0.0.1:8000/blog/list/
    path("list/", blog_list),
    # http://127.0.0.1:8000/blog/list2/
    path("list2/", BlogListView.as_view()),
]