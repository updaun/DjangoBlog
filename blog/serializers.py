from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Blog


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # exclude = ('password',)
        fields = (
            "id",
            "username",
            "email",
        )


class BlogSerializer(serializers.ModelSerializer):
    # user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=True)
    user = UserSerializer(read_only=True)
    class Meta:
        model = Blog
        fields = '__all__'