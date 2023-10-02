from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("author/", views.author_read, name="author_read"),
    path("article/", views.article_read, name="article_read"),
    path("articles_by_author/", views.articles_by_author, name="articles_by_author"),
]
