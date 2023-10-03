from django.shortcuts import render, get_object_or_404
from online_store_app.models import Client, Product, Order


def index(request):
    clients = Client.objects.all()
    context = {"title": "Все клиенты", "clients": clients}
    return render(request, "online_store_app/index.html", context)