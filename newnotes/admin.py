from django.contrib import admin
from .models import Article, Comment, Category, ArticleUserRelation, ArticleCategoryRelation

admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(ArticleUserRelation)
admin.site.register(ArticleCategoryRelation)
