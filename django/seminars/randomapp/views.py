from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.


def get_eagle_or_tails(request) -> str:
    result = bool(random.getrandbits(1))
    return HttpResponse(f"{'Выпала Решка' if result else 'Выпал Орёл'}")


def get_side_cube(request) -> str:
    result = random.randint(1, 6)
    return HttpResponse(f"Выпало {result} точек на кубике")


def get_rnd_num(request) -> str:
    result = random.randint(0, 100)
    return HttpResponse(f"Выпало число {result}")