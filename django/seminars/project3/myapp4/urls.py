from django.urls import path
from myapp4 import views

urlpatterns = [
    path("games/", views.choice_games_form, name="choice_games_form"),
]