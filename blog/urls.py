from django.urls import path, include
from .views import *

# http://127.0.0.1:8000/blog/
urlpatterns = [
    # http://127.0.0.1:8000/blog/list/
    path("list/", blog_list),
    path("list2/", BlogListView.as_view()),
    # http://127.0.0.1:8000/blog/3/
    path("<int:blogid>/", BlogDetailView.as_view()),
]