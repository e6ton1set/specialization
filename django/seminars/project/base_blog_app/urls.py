from django.urls import path
from . import views

urlpatterns = [
    path("", views.author_read, name="author_read"),
]
