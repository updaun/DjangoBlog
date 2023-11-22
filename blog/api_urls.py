from django.urls import path, include
from .apis import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("", BlogViewSet)


# http://127.0.0.1:8000/api/blog/
urlpatterns = [
    # http://127.0.0.1:8000/api/blog/
    path("",BlogAPI.as_view()),        

    # http://127.0.0.1:8000/api/blog/generic/
    path("generic/",BlogGenericAPI.as_view()),

    # http://127.0.0.1:8000/api/blog/<int:pk>/
    path("<int:pk>/",BlogDetailAPI.as_view()),

    # http://127.0.0.1:8000/api/blog/generic/<int:pk>/
    path("generic/<int:pk>/",BlogGenericDetailAPI.as_view()),

    # router.register("viewset", BlogViewSet) 으로 하고 
    # path("",include(router.urls)) 로 해도 된다.
    # path가 빈 문자열로 한다면, urlpatterns 위에서부터 url을 타기 때문에 조심해야 할 필요가 있다.
    # ( "" 처럼 빈 문자열이 겹치기 때문에, path("",BlogAPI.as_view()), 이걸 타게 되기 때문이다.)
    
    # 지금 방식으로 하면, path 마지막에 '/'를 꼭 붙여줘야 한다.
    path("viewset/",include(router.urls)),

    # http://127.0.0.1:8000/api/blog/hello/
    path("hello/",HelloWorldAPI.as_view()),

]

# get만 redirect (301)해서 "/"없이도 보여주지만, 나머지는 "/"가 필수다.
# 다른 메소드는 "/"에 민감하다
# 더 restful 하다고는 하는데,"/"는 회사마다 다르다.