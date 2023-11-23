from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, viewsets
from .models import Blog
from .serializers import BlogSerializer
from rest_framework import exceptions
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated



class HelloWorldAPI(APIView):
    def get(self, request):
        return Response(status=status.HTTP_200_OK, data={"method":"get"})

    def post(self, request):
        return Response(status=status.HTTP_201_CREATED, data={"method":"post"})

    def put(self, request):
        return Response(status=status.HTTP_200_OK, data={"method":"put"})

    def patch(self, request):
        return Response(status=status.HTTP_200_OK, data={"method":"patch"})

    def delete(self, request):
        return Response(status=status.HTTP_200_OK, data={"method":"delete",
                                                         "message":"데이터가 잘 삭제되었습니다."})
    

class BlogAPI(APIView):

    # blog list -> serializer -> json -> response
    def get(self, request):
        blog_list = Blog.objects.all() # QuerySet blog model이 여러 개
        serializer = BlogSerializer(blog_list, many=True) 
        return Response(data={"blog_list":serializer.data})
    
    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        blog = serializer.save()
        serializer = BlogSerializer(blog)
        return Response(status=status.HTTP_201_CREATED, data={"blog":serializer.data})


class BlogGenericAPI(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogDetailAPI(APIView):

    def get_object(self, pk):
        try:
            blog = Blog.objects.get(pk=pk)
        except Blog.DoesNotExist:
            raise exceptions.NotFound(detail="해당 블로그를 찾을 수 없습니다.")
        return blog

    def get(self, request, pk):
        blog = self.get_object(pk)
        serializer = BlogSerializer(blog)
        return Response(status=status.HTTP_200_OK, data={"blog":serializer.data})
    
    def put(self, request, pk):
        blog = self.get_object(pk)
        serializer = BlogSerializer(blog, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data={"message":"블로그가 수정되었습니다.", "data":serializer.data})
    
    def patch(self, request, pk):
        blog = self.get_object(pk)
        serializer = BlogSerializer(blog, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data={"message":"블로그가 수정되었습니다.", "data":serializer.data})
    
    def delete(self, request, pk):
        blog = self.get_object(pk)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class BlogGenericDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
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