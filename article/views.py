from django.shortcuts import render
from article.models import Article, Comment
from rest_framework import viewsets, generics
from rest_framework import permissions
from .serializer import ArticleSerializer, CommentCreateSerializer, CommentSerializer

# Create your views here.
# some_app/views.py
from django.views.generic import TemplateView



class ArticleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class CommentViewSet(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        queryset = self.queryset
        if self.kwargs.get('article_id', None):
            queryset = queryset.filter(article__id=self.kwargs['article_id'])

        return queryset


class CommentCreateViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer