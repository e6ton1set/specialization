from django.urls import path
from . import views

urlpatterns = [
    path("game1/", views.get_eagle_or_tails, name="get_eagle_or_tails"),
    path("game2/", views.get_side_cube, name="get_side_cube"),
    path("game3/", views.get_rnd_num, name="get_rnd_num"),
]
