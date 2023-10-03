from django.shortcuts import render
import random
import logging

HISTORY = {
    "et": [],
    "sc": [],
    "rn": [],
}

logger = logging.getLogger(__name__)


def index2(request):
    logger.info("index.html is used")
    context = {"index2": "Главная страница"}
    return render(request, "myapp2/index.html", context)


def about2(request):
    logger.info("about.html is used")
    context = {"about2": "Информация"}
    return render(request, "myapp2/about.html", context)


def statistic(request) -> str:
    logger.info("Statistic used")
    context = {
        "et": HISTORY["et"],
        "sc": HISTORY["sc"],
        "rn": HISTORY["rn"],
    }
    return render(request, "myapp2/statistic.html", context)


def get_eagle_or_tails(request, trial) -> str:
    name_game = "get_eagle_or_tails"
    logger.info("Game 1 is used")
    context = {"res": [], "name_game": name_game}
    while trial > 0:
        result = bool(random.getrandbits(1))
        context["res"].append(f"{'Выпала Решка' if result else 'Выпал Орёл'}")
        HISTORY["et"].append(f"{'Выпала Решка' if result else 'Выпал Орёл'}")
        trial -= 1
    return render(request, "myapp2/player.html", context)


def get_side_cube(request, trial) -> str:
    name_game = "get_side_cube"
    logger.info("Game 2 is used")
    context = {"res": [], "name_game": name_game}
    while trial > 0:
        result = random.randint(1, 6)
        context["res"].append(result)
        HISTORY["sc"].append(result)
        trial -= 1
    return render(request, "myapp2/player.html", context)


def get_rnd_num(request, trial) -> str:
    name_game = "get_rnd_num"
    logger.info("Game 3 is used")
    context = {"res": [], "name_game": name_game}
    while trial > 0:
        result = random.randint(0, 100)
        context["res"].append(result)
        HISTORY["rn"].append(result)
        trial -= 1
    return render(request, "myapp2/player.html", context)
