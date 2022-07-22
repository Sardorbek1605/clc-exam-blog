from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Article, Comment


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('__all__')
        depth = 1


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('__all__')


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('__all__')