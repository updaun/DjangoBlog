from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework import exceptions
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication

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

    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        blog = serializer.save()
        serializer = BlogSerializer(blog)
        return Response(status=status.HTTP_201_CREATED, data={"blog": serializer.data})
        
class BlogGenericAPI(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogDetailAPI(APIView):

    def get_object(self, pk):        
        try:
            blog = Blog.objects.get(pk=pk)
        except Blog.DoesNotExist:
            raise exceptions.NotFound(detail = "not found") 
        return blog

    def get(self, request, pk):
        blog = self.get_object(pk)
        serializer = BlogSerializer(blog, many=False)
        return Response(status=status.HTTP_200_OK, data={"blog": serializer.data})
    
    def put(self, request, pk):
        blog = self.get_object(pk)
        serializer = BlogSerializer(blog , data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK, data={"message": "change blog", "data": serializer.data})
    
    # https://cdrf.co
    def patch(self, request, pk):
        blog = self.get_object(pk)
        serializer = BlogSerializer(blog , data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK, data={"message": "change blog", "data": serializer.data})
    
    def delete(self, request, pk):
        blog = self.get_object(pk)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class BlogGerericDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    # authentication_classes = (SessionAuthentication)
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        print(self.request.user)
        serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)