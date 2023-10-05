import datetime
from django import forms

from base_blog_app import models


class AuthorForm(forms.Form):
    first_name = forms.CharField(label="",
                                 max_length=30,
                                 widget=forms.TextInput(
                                     attrs={"class": "input-text long-input",
                                            "placeholder": "Имя автора"}))
    last_name = forms.CharField(label="",
                                widget=forms.TextInput(
                                    attrs={"class": "input-text long-input",
                                           "placeholder": "Отчество автора"}))
    email = forms.EmailField(label="",
                             widget=forms.EmailInput(attrs={"class": "input-text long-input",
                                                            "type": "email",
                                                            "placeholder": "Email автора"}))
    biography = forms.CharField(initial="Биография:",
                                label="",
                                widget=forms.Textarea(attrs={"class": "input-text long_input"}))
    birthday = forms.DateField(initial=datetime.date.today(),
                               label="",
                               widget=forms.DateInput(attrs={"class": "input-text long-input",
                                                             'type': "date"}))


class ArticleForm(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ["author", "title", "content", "author", "is_published"]
        labels = {"author": "", "title": "", "content": "", "is_published": ""}
        widgets = {
            "author": forms.Select(attrs={"class": "input-text long-input", "placeholder": "Выберите автора"}),
            "title": forms.TextInput(attrs={"class": "input-text long-input", "placeholder": "Название статьи"}),
            "content": forms.Textarea(attrs={"class": "input-text long_input", "placeholder": "Текст статьи"})}


class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ["author", "article", "comment"]
        labels = {"author": "", "article": "", "comment": ""}
        widgets = {
            "author": forms.Select(attrs={"class": "input-text long-input", "placeholder": "Выберите автора"}),
            "article": forms.Select(attrs={"class": "input-text long-input", "placeholder": "Выберите статью"}),
            "comment": forms.Textarea(attrs={"class": "input-text long_input", "placeholder": "Текст комментария"})}