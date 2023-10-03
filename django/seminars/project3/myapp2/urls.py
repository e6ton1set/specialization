from django.urls import path
from myapp2 import views

urlpatterns = [
    path("game1/<int:trial>/", views.get_eagle_or_tails, name="get_eagle_or_tails"),
    path("game2/<int:trial>/", views.get_side_cube, name="get_side_cube"),
    path("game3/<int:trial>/", views.get_rnd_num, name="get_rnd_num"),
    path("statistic/", views.statistic, name="statistic"),
    path("index2/", views.index2, name="index2"),
    path("about2/", views.about2, name="about2"),
]