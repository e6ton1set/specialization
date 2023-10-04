from datetime import timedelta

from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from online_store_app.models import Client, Product, Order


def index(request):
    clients = Client.objects.all()
    context = {"title": "Все клиенты", "clients": clients}
    return render(request, "online_store_app/index.html", context)


def all_orders(request, client_id):
    client = Client.objects.get(pk=client_id)
    all_orders = {"unique_order": [], "products": []}
    orders = Order.objects.all()
    length_key = len(all_orders)

    for order in orders:
        if client_id == order.customer_id:
            all_orders["unique_order"].append(order.id)

    while length_key != 0:
        curr_order = get_object_or_404(Order, pk=client_id)
        products = Product.objects.filter(order=curr_order).all()
        all_orders["products"].append(products)
        length_key -= 1

    context = {"all_orders": all_orders, "client": client, "order": curr_order}

    return render(request, "online_store_app/all_orders.html", context)


def orders_by_time(request):
    clients = Client.objects.all()
    context = {
        'clients': clients
    }
    if request.method == 'POST':
        client_id = request.POST.get('client_id')
        client = Client.objects.get(id=client_id)
        days = request.POST.get('report')
        if days == '7':
            orders = Order.objects.filter(customer=client, date_ordered=timezone.now() - timedelta(days=7))
            time_period = 'неделю'
        elif days == '30':
            orders = Order.objects.filter(customer=client, date_ordered=timezone.now() - timedelta(days=30))
            time_period = 'месяц'
        else:
            orders = Order.objects.filter(customer=client, date_ordered=timezone.now() - timedelta(days=365))
            time_period = 'год'
        products = []
        for order in orders:
            products.extend(order.products.all())
        products = list(set(products))
        context.update({
            'client': client,
            'products': products,
            'days': time_period
        })
    return render(request, 'online_store_app/orders_by_time.html', context)
