from django.http import HttpResponse
import logging
from django.shortcuts import render, get_object_or_404

from base_blog_app.models import Author, Article, Comment

logger = logging.getLogger(__name__)


def index(request):
    return HttpResponse(f"Index HTML")


def author_read(request):
    logger.info(f"Чтение авторов (подробности: {request}")
    authors = Author.objects.all()
    return HttpResponse(authors)


def article_read(request):
    logger.info(f"Чтение публикаций (подробности: {request}")
    articles = Article.objects.all()
    return HttpResponse(articles)


def articles_by_author(request):
    logger.info(f"Запрос статей по ID автора: {request}")
    name = request.GET.get("name")
    author_id = Author.objects.filter(first_name=name).first()
    articles_author = Article.objects.filter(author_id=author_id).all()
    return HttpResponse(articles_author)


def view_all_articles(request):
    articles = Article.objects.all()
    context = {"title": "Список статей", "articles": articles}

    return render(request, "base_blog_app/template_articles.html", context)


def view_article(request, article_id):
    article = Article.objects.get(id=article_id)
    context = {"title": article.title, "text": article.content}

    article.show_count += 1
    article.save()

    return render(request, "base_blog_app/template_article.html", context)


def view_comment_article(request, post_id):
    article = get_object_or_404(Article, pk=post_id)
    comments = Comment.objects.filter(article=article).all()
    article.show_count += 1
    article.save()

    return render(request, "base_blog_app/template_comment.html", {"article": article,
                                                                   "comments": comments,
                                                                   "show_count": article.show_count
                                                                   }
                  )
