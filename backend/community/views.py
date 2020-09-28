from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.forms.models import model_to_dict
from .serializers import ArticleSerializer, ArticleListSerializer
from .models import Article

@permission_classes((AllowAny,))
class CommunityList(APIView):
    queryset = Article.objects.all()

    
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)


    @permission_classes([IsAuthenticated])
    def post(self, request):
        article = Article(title=request.data['title'],content=request.data['content'],user=request.user)
        article.save()
        return Response(status=status.HTTP_201_CREATED)

@permission_classes((AllowAny,))
class CommunityDetail(APIView):
    queryset = Article.objects.all()

    def get(self, request, article_pk):
        article = get_object_or_404(Article, pk=article_pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)


    @permission_classes([IsAuthenticated])
    def delete(self, request, article_pk):
        article = Article.objects.get(pk=article_pk)
        if request.user.user_id == article.user_id:
            article.delete()
        return Response(status=status.HTTP_200_OK)


    @permission_classes([IsAuthenticated])
    def put(self, request, article_pk):
        article = get_object_or_404(Article, pk=article_pk)
        serializer = ArticleSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data)
