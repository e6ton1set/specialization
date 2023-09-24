from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    biography = models.TextField()
    birthday = models.DateTimeField()

    def get_full_name(self):
        full_name = f"{self.first_name} {self.last_name}"
        return full_name

    def __str__(self):
        return f"{self.first_name}"


class Article(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    published = models.DateTimeField()
    category = models.CharField(max_length=200)
    show_count = models.IntegerField(default=0)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}"