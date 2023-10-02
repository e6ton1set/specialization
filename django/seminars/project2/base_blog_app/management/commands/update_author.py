from django.core.management import BaseCommand
from base_blog_app.models import Author, Article


class Command(BaseCommand):
    help = "Update author by ID"

    def add_arguments(self, parser):
        parser.add_argument("pk", type=int, help="Author ID")
        parser.add_argument("email", type=str, help="Author email")

    def handle(self, *args, **kwargs):
        pk = kwargs.get("pk")
        author = Author.objects.filter(pk=pk).first()
        email = kwargs.get("email")
        author.email = email
        author.save()
        self.stdout.write(f"Update email by: {author}")
