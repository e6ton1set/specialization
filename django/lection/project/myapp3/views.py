from django.http import HttpResponse, JsonResponse
from django.views import View
from django.shortcuts import render


def hello(request):
    return HttpResponse("It's view-function!")


class HelloView(View):
    @staticmethod
    def get(request):
        return HttpResponse("It's view-Class")


def year_post(request, year):
    res = [1, 2, 3, 4, 5]
    ...
    return HttpResponse(f"Posts from {year}<br> {[num * 2 for num in res]}")


class MonthPost(View):
    def get(self, request, year, month):
        res = [1, 2, 3, 4, 5]
        ...
        return HttpResponse(f"Posts from {month}/{year}<br> {[num * 2 for num in res]}")


def post_detail(request, year, month, slug):
    posts = {
        "year": year,
        "month": month,
        "slug": slug,
        "title": "Кто быстрее создаёт списки в Python: list() или []",
        "content": "Текст"
    }
    return JsonResponse(posts, json_dumps_params={"ensure_ascii": False})


def index(request):
    context = {"name": "Руслан",
               "content": [1, 2, 3, 4, 5]
               }
    return render(request, "myapp3/index.html", context)