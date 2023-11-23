from django.urls import path, include
from .views import blog_list,BlogListView,BlogDetailView,BlogCreateView,BlogUpdateView
from .apis import *

# 기본 라우팅 자체가 blog부터 시작
# http://127.0.0.1:8000/blog/
# 라우팅은 urlpatterns 에 작성된 순서대로 찾아나간다.
urlpatterns = [
    # http://127.0.0.1:8000/blog/api/hello/
    path("api/hello/",HelloWorldAPI.as_view()),

    # http://127.0.0.1:8000/blog/list/
    path("list/",blog_list),

    # http://127.0.0.1:8000/blog/list2/
    # 함수가 아니라, 클래스일 때는 .as_view()를 붙여줘야 한다.
    path("list2/",BlogListView.as_view()),
    
    # http://127.0.0.1:8000/blog/3/
    # pk가 관념적인 룰(blogid, id 등으로 바꿔도 된다.)
    path("<int:blogid>/",BlogDetailView.as_view()),

    path("create/",BlogCreateView.as_view()),

    path("update/<int:pk>/", BlogUpdateView.as_view())
]
