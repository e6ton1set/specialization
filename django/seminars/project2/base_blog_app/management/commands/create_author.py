from abc import ABC
from django.core.management import BaseCommand
from base_blog_app.models import Author, Article


class Command(BaseCommand, ABC):
    help = "Generate fake authors and articles"

    def add_arguments(self, parser):
        parser.add_argument("count", type=int, help="Count authors")

    def handle(self, *args, **kwargs):
        count = kwargs.get("count")
        for i in range(1, count + 1):
            author = Author(first_name=f"Name_{i}", email=f"mail_{i}@mail.ru")
            author.save()
            for j in range(1, count + 1):
                article = Article(
                    title=f"Title{j}",
                    content=f"Text from {author.first_name} #_{j} bla-bla-bla",
                    author=author,
                    is_published=True,
                )
                article.save()
                for k in range(1, count + 1):
                    comment = Comment(
                        comment=f"Text from # bla-bla-bla",
                        author=author,
                        article=article,
                    )
                    comment.save()