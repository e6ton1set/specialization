from django.core.management import BaseCommand
from base_blog_app.models import Author, Article


class Command(BaseCommand):
    help = "Delete author by ID"

    def add_arguments(self, parser):
        parser.add_argument("pk", type=int, help="Author ID")

    def handle(self, *args, **kwargs):
        pk = kwargs.get("pk")
        author = Author.objects.filter(pk=pk).first()
        author.delete()
        self.stdout.write(f"Author deleted: {author}")
