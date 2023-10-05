from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("all_orders/<int:client_id>", views.all_orders, name="all_orders"),
    path("orders_by_time/", views.orders_by_time, name="orders_by_time"),
    path("upload_image/", views.upload_image, name="upload_image"),
]