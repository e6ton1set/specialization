from django.core.management import BaseCommand
from base_blog_app.models import Author, Article, Comment


class Command(BaseCommand):
    help = "Generate fake comments"

    def add_arguments(self, parser):
        parser.add_argument("author_id", type=int, help="Author ID")

    def handle(self, *args, **kwargs):
        author_id = kwargs.get("author_id")
        author = Author.objects.filter(pk=author_id).first()
        articles = Article.objects.filter(author=author_id).all()
        for article in articles:
            comment = Comment(author=author, article=article, comment="Комментарий")
            comment.save()
