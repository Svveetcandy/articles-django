from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'newnotes'
urlpatterns = [
	path('profile/', views.profile, name='profile'),
	path('register/', views.register, name='register'),
	path('articles/create/', views.create_article, name='create_article'),
	path('articles/<int:article_id>/', views.ViewArticle.as_view(), name='view_article'),
	path('articles/update/<int:article_id>/', views.update_article, name='update_article'),
	path('articles/delete/<int:article_id>/', views.delete_article, name='delete_article'),
	path('articles/<int:article_id>/leave_comment/', views.leave_comment, name='leave_comment'),
	path('articles/', views.ArticleListView.as_view(), name='list_articles'),
	path('categories/<int:category_id>/', views.ListCategoryArticles.as_view(), name='view_category'),
	path('categories/create/', views.create_category, name='create_category'),
	path('categories/delete/<int:category_id>/', views.delete_category, name='delete_category'),
	path('categories/update/<int:category_id>/', views.update_category, name='update_category'),
	path('', views.index, name='index'),
]