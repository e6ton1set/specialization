import datetime as dt
from django.db import models
from django.utils.timezone import now


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, default="None")
    email = models.EmailField()
    biography = models.TextField(default="None")
    birthday = models.DateField(default=dt.date.today())

    def get_full_name(self):
        full_name = f"{self.first_name} {self.last_name}"
        return full_name

    def __str__(self):
        return f"{self.first_name}"


class Article(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    published = models.DateField(default=dt.date.today())
    category = models.CharField(max_length=200, default="category")
    show_count = models.IntegerField(default=0)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}"


class Comment(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=4)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, default=4)
    comment = models.TextField()
    is_published = models.DateTimeField(default=now)
    updated = models.DateTimeField(default=now)

    def __str__(self):
        return f"Title is {self.comment}"
