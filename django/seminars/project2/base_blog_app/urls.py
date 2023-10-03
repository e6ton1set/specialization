from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("author/", views.author_read, name="author_read"),
    path("article/", views.article_read, name="article_read"),
    path("articles_by_author/", views.articles_by_author, name="articles_by_author"),
    path("view_all_articles/", views.view_all_articles, name="view_all_articles"),
    path("view_article/<int:article_id>", views.view_article, name="view_article"),
    path("view_comment_article/<int:post_id>", views.view_comment_article, name="view_comment_article"),
]
