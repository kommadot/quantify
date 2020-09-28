from rest_framework import serializers
from users.serializers import CustomUserSerializer, UserSerializer
from .models import Article


# index
class ArticleListSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()
    # username = user.username

    class Meta:
        model = Article
        fields = (
            'id',
            'title',
            'user',
            'created_at',
        )


# detail
class ArticleSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = Article
        fields = (
            'id',
            'title',
            'content',
            'user',
            'created_at',
            'updated_at'
        )
