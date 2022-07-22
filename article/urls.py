from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ArticleViewSet.as_view()),
    path('/<int:article_id>/messages', views.MessageCreateViewSet.as_view())
]