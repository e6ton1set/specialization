from django.http import HttpResponse
import logging
from base_blog_app.models import Author, Article

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
