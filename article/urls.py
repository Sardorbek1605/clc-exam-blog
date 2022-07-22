from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('/', views.ArticleViewSet.as_view()),
    path('/<int:id>/', views.ArticleRetrieveViewSet.as_view()),
    path('/<int:article_id>/comments', views.CommentViewSet.as_view()),
    path('/<int:article_id>/comments/create', views.CommentCreateViewSet.as_view())
]