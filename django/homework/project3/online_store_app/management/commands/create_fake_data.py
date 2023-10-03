from django.core.management import BaseCommand
from online_store_app.models import Client, Product, Order
import random


class Command(BaseCommand):
    help = "Generate fake data: clients, products, orders"

    def add_arguments(self, parser):
        parser.add_argument("count", type=int, help="Amount clients")

    def handle(self, *args, **kwargs):
        count = kwargs.get("count")
        clientele_list = []
        products_list = []

        for i in range(1, count + 1):
            client = Client(
                name=f"Name_{i}",
                email=f"email_{i}@ya.ru",
                phone=f"Phone_{i}",
                address=f"Street_{i}"
            )
            client.save()
            clientele_list.append(client)

            for j in range(1, count + 1):
                product = Product(
                    name=f"Product_{j}",
                    amount=f"{j * random.randint(1, 32)}",
                    price=f"{j * random.randint(1, 4096)}"
                )
                product.save()
                products_list.append(product)

        for k in range(1, count + 1):
            client_rnd = random.randint(1, count - 1)
            order = Order(customer=clientele_list[client_rnd])
            total_price = 0
            for l in range(0, count - 1):
                total_price += float(products_list[l].price)
                order.total_price = total_price
                order.save()
                order.products.add(products_list[l])

        self.stdout.write(f"Created: {count} fake clients.")