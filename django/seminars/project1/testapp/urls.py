from django.urls import path
from testproject.testapp import views

urlpatterns = [
    path("", views.testapp, name="testapp"),
    path("game1/", views.eagle_or_tails, name="game1"),
]
