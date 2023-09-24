from django.shortcuts import render
from django.http import HttpResponse
import random
import logging

# Create your views here.

logger = logging.getLogger(__name__)


def get_eagle_or_tails(request) -> str:
    logger.info("Game 1 is used")
    result = bool(random.getrandbits(1))
    return HttpResponse(f"{'Выпала Решка' if result else 'Выпал Орёл'}")


def get_side_cube(request) -> str:
    logger.info("Game 2 is used")
    result = random.randint(1, 6)
    return HttpResponse(f"Выпало {result} точек на кубике")


def get_rnd_num(request) -> str:
    logger.info("Game 3 is used")
    result = random.randint(0, 100)
    return HttpResponse(f"Выпало число {result}")