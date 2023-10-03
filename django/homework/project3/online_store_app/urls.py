from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("all_orders/<int:client_id>", views.all_orders, name="all_orders"),
]