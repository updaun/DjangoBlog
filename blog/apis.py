from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, viewsets
from .models import Blog
from .serializers import BlogSerializer
from rest_framework import exceptions


# 원래 API 마다 authentication_classes 과 permission_classes를 설정해줘야 하지만,
# 이미 settings에 authentication_classes를 디폴트로 넣어놨다.
# 특정 API 는 다른 인증방식을 사용하고 싶으면 해당 API에서 특정 인증방식으로 덮으면 된다.

from rest_framework.authentication import SessionAuthentication 
from rest_framework.permissions import IsAuthenticated




class HelloWorldAPI(APIView):

    def get(self,request):
        return Response(status=status.HTTP_200_OK, data={"method":"get"})

    def post(self,request):
        return Response(status=status.HTTP_201_CREATED,data={"method":"post"})

    def put(self,request):
        return Response(staus=status.HTTP_200_OK,data={"method":"put"})

    def patch(self,request):
        return Response(status=status.HTTP_200_OK,data={"method":"patch"})

    # 204로 status 하면 데이터 리턴이 안됨 그래서 보통 200으로 놔두고, 메시지를 만진다.
    def delete(self,request):
        return Response(status=status.HTTP_200_OK,data={"method":"delete","message":"데이터가 잘 삭제되었습니다"})
        # return Response(status=status.HTTP_204_NO_CONTENT,data={"method":"delete"})


# 전체 Blog 리스트 조회, 생성
class BlogAPI(APIView):

    # blog -> serializer -> json -> response

    def get(self,request):

        blog_list = Blog.objects.all() # QuerySet Models - blog Model이 여러 개 
        serializer = BlogSerializer(blog_list,many=True) # 쿼리셋이기에 many=True 
        # 모델을 json 형태로 만드는 serializer
        return Response(data={"blog_list":serializer.data})

    def post(self,request):
        
        #  Serializer 첫번째 인자는 인스턴스여야 한다. (data=로 작성)
        serializer = BlogSerializer(data=request.data)
        
        # 모델에 정의해 놓은 제약사항 기준으로 요청데이터를 검증한다.(True or False를 반환)
        # if, else 보다 raise_exception=True로 하면 더 깔끔한 코드가 된다.(오류면 여기서 멈춤)
        serializer.is_valid(raise_exception=True)
        # True라면 진행
        blog = serializer.save()

        # user의 point가 차감되도록 코딩하면 
        # user.point -= 100
        # blog.save() 해줘야 한다.
        serializer = BlogSerializer(blog)
        return Response(status=status.HTTP_201_CREATED, data={"blog":serializer.data})

# generics API를 사용하면 위의 클래스 기능과 동일하다!
# ListAPIView 와 CreateAPIView 둘 다 포함하는 ListCreateAPIView
class BlogGenericAPI(generics.ListCreateAPIView):
    
    queryset = Blog.objects.all().order_by("-created_at")   # 최신 순으로 정렬
    serializer_class = BlogSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = self.queryset
        queryset = queryset.filter(user=self.request.user)  # 본인 것만 filter
        
        
        # http://127.0.0.1:8000/blog/generic/?title=테스트
        # querystring으로 title로 검색(검색을 간단하게 구현)
        title = self.request.query_params.get("title")
        if title:
            queryset = queryset.filter(title__icontains=title)

        return queryset





# 상세 조회
class BlogDetailAPI(APIView):

    # get_object 라는 메소드를 오버라이딩한다.(계속 반복되는 로직이니까(get_object라는 메소드는 실제로 있으니까 오버라이딩해야함))
    def get_object(self,pk):
        try:
            blog = Blog.objects.get(pk=pk)
        
        except Blog.DoesNotExist:   # pk가 없는 pk 일 때는 except Blog.DoesNotExist 탄다.
            raise exceptions.NotFound(detail="해당 블로그를 찾을 수 없습니다.")
            # return Response(status=status.HTTP_404_NOT_FOUND, data  = {"message":"존재하지 않는 블로그입니다."})
        return blog

    def get(self,request,pk):
        try:
            blog = Blog.objects.get(pk=pk)
        
        except Blog.DoesNotExist:   # pk가 없는 pk 일 때는 except Blog.DoesNotExist 탄다.
            return Response(status=status.HTTP_404_NOT_FOUND, data  = {"message":"존재하지 않는 블로그입니다."})
        
        # except에 안 걸리면 존재하는 글
        
        serializer = BlogSerializer(blog)   #한 개만 가져오니까 many=True 안해도 된다.

        return Response(status=status.HTTP_200_OK, data={"blog":serializer.data})
    
    # put은 "전체" 데이터를 보내줘야만 해당 요청에 따라 수정해준다.
    def put(self,request,pk):

        blog = self.get_object(pk)
        serializer = BlogSerializer(blog,data=request.data)
        # 바로 수정하지 말고, 검증과정을 항상 거쳐야 한다.
        serializer.is_valid(raise_exception=True)
        # 검증완료됐으면   
        serializer.save()

        return Response(data={"message":"블로그가 수정되었습니다.","data":serializer.data})
    

    # patch는 "부분"데이터를 보내도 해당 요청에 따라 수정해준다.
    def patch(self,request,pk):

        blog = self.get_object(pk)
        serializer = BlogSerializer(blog,data=request.data, partial=True)
        # 바로 수정하지 말고, 검증과정을 항상 거쳐야 한다.
        serializer.is_valid(raise_exception=True)
        # 검증완료됐으면   
        serializer.save()

        return Response(data={"message":"블로그가 수정되었습니다.","data":serializer.data})
    

    # 정석은 patch가 부분 수정이지만, 어떤 회사에서는 전체든 일부든 수정을 다 put으로 하고, partial=True를 주기도 한다.
    # 정석은 patch에만 일부 수정을 허용하는 것이다.


    def delete(self,request,pk):

        blog = self.get_object(pk)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Retrieve는 상세조회만
# UpdateAPIView는 업데이트만
# DestroyAPIView는 Delete 기능을 하는 API

# 이 세가지를 다 하는 APIVIew가 바로 RetrieveUpdateDestroyAPIView 이다.
class BlogGenericDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    # 필요할 때는 .filter()를 사용해서 범위를 좁혀낼 수 있다. 일단은 all() 을 해주자.
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


# ListCreateAPIView 와 RetrieveUpdateDestroyAPIView 를 다 합치는 ViewSets
class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all().order_by('-created_at')   # -를 붙였으니까 최신순으로 정렬
    serializer_class = BlogSerializer
    # # 인증
    # authentication_classes = ()
    # 인가
    permission_classes = (IsAuthenticated,)

    # # 방법 1) update랑 delete를 막기보다는 보여지는 list를 해당 유저가 생성한 글만 보여지도록 한다.
    # def get_queryset(self):
    #     queryset = self.queryset
    #     queryset = queryset.filter(user=self.request.user)
    #     return queryset

    # 아래 perform_create 나 create는 쓰나 안쓰나 viewset에 원래 적용된 메소드로 똑같지만, 
    # 수정하려고 해당 함수를 명시해서 수정하려고 한다. 지금은 save() 인자에 ser=self.request.user 를 줬다.
    def perform_create(self,serializer):
        print(self.request.user)
        serializer.save(user=self.request.user)

    # 결론적으로 create 함수는 바꾼게 없지만, 공부목적상 적어두자. perform_create를 통해 user가 쏙 들어가게 됐다.
    def create(self, request, *args, **kwargs):
        # user = request.user
        # 둘 다 똑같다.
        # user = self.request.user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    # 안 써도 default이지만 일단 눈에 익게 써놓자.(https://www.cdrf.co/3.14/rest_framework.viewsets/ModelViewSet.html)
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    
    # 방법 2) 지금은 방법 1 때문에 이거 안 탄다.
    def update(self,request, *args,**kwargs):

        partial = kwargs.pop('partial',False)
        instance = self.get_object()

        if instance.user != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance,'_prefetched_objects_cache',None):

            instance._prefetched_objects_cahce = {}
        
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        if instance.user != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        return Response(status=status.HTTP_204_NO_CONTENT)
