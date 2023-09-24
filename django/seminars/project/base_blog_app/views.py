from django.http import HttpResponse
import logging
from base_blog_app.models import Author

logger = logging.getLogger(__name__)


def author_read(request):
    logger.info(f"Чтение авторов (подробности: {request}")
    authors = Author.objects.all()
    return HttpResponse(authors)
