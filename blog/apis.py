from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Blog
from .serializers import BlogSerializer

class HelloWorldAPI(APIView):

    def get(self, request):
        return Response(status=status.HTTP_200_OK, data={"method": "get"})

    def post(self, request):
        return Response(status=status.HTTP_201_CREATED, data={"method": "post"})

    def put(self, request):
        return Response(status=status.HTTP_200_OK, data={"method": "put"})
    
    def patch(self, request):
        return Response(status=status.HTTP_200_OK, data={"method": "patch"})

    def delete(self, request):
        # 204 는 data 가 있어도 반환되지 않는다.
        return Response(status=status.HTTP_204_NO_CONTENT, data={"method": "delete"})
    

class BlogAPI(APIView):
    def get(self, request):
        blog_list = Blog.objects.all()
        serializer = BlogSerializer(blog_list, many=True)
        return Response(data={"blog_list": serializer.data})
        