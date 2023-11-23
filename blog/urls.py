from django.urls import path, include
from . import views

urlpatterns = [

    path("list/", views.blog_list),
    path("list2/", views.BlogListView.as_view()),
    path("<int:pk>/", views.BlogDetailView.as_view()),

    path("create/", views.BlogCreateView.as_view()),
    path("update/<int:pk>/", views.BlogUpdateView.as_view()),
]