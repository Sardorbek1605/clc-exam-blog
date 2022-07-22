from django.db import models
from helpers.models import BaseModel
from common.models import User

# Create your models here.


class ArticleQuerySet(models.QuerySet):
    def is_popular(self):
        return self.filter(is_popular=True)


class ArticleManager(models.Manager):
    def get_queryset(self):
        return ArticleQuerySet(self.model, using=self._db)

    def is_popular(self):
        return self.get_queryset().is_popular()


class Article(BaseModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=128, unique=True)
    description = models.TextField()
    content = models.TextField()
    image = models.ImageField(upload_to='article/')
    is_popular = models.BooleanField(default=False)
    object = ArticleManager
    print(object.is_popular)


class Comment(BaseModel):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    message = models.TextField()



