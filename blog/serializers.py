from rest_framework import serializers
from .models import Blog

class BlogSerializer(serializers.ModelSerializer):

    # meta 속성을 써준 이유는 장고에서 Modelclass는 self.meta.model 형식으로 정의되기 떄문이다!
    class Meta:
        model = Blog
        fields = "__all__"
