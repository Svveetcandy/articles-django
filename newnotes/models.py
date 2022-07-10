from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    article = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField('тема', max_length=250)
    text = models.TextField('текст')
    date = models.DateTimeField('дата')
    readers = models.ManyToManyField(User, through='ArticleUserRelation', related_name='my_articles')

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField('название', max_length=50)
    includes_article = models.ManyToManyField(Article, through='ArticleCategoryRelation')


class Comment(models.Model):
    comment = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.CharField('автор', max_length=150)
    text = models.CharField('текст', max_length=500)
    date = models.DateTimeField('дата')


class ArticleUserRelation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    is_watched = models.BooleanField(default=False)


class ArticleCategoryRelation(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
