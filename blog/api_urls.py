from django.urls import path, include
from .apis import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("", BlogViewSet)

# http://127.0.0.1:8000/api/blog/
urlpatterns = [
    path("", BlogAPI.as_view()),
    path("generic/", BlogGenericAPI.as_view()),
    path("<int:pk>/", BlogDetailAPI.as_view()), 
    path("generic/<int:pk>/", BlogGenericDetailAPI.as_view()),
    path("viewset/", include(router.urls)),
    # http://127.0.0.1:8000/api/blog/hello/
    path("hello/", HelloWorldAPI.as_view()),
]