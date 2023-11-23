from rest_framework import serializers
from .models import Blog
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        # 이렇게 넘기고 싶은 정보만 적어주는 방법도 있고
        fields = (
            "id",
            "username",
            "email",
        )
        
        # exclude 처럼 모든 필드 정보 중에서 제외시킬 정보만 적어주는 방법도 있다.
        # exclude = ("password",) 


class BlogSerializer(serializers.ModelSerializer):
    # user를 아무리 넣으려고 해도 무시된다.
    user = UserSerializer(read_only=True)
    # meta 속성을 써준 이유는 장고에서 Modelclass는 self.meta.model 형식으로 정의되기 떄문이다!
    class Meta:
        model = Blog
        fields = "__all__"
