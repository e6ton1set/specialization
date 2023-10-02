from django.shortcuts import render


def index(request):
    context = {"name": "Руслан"}
    return render(request, "myapp/index.html", context)


def about(request):
    facts = {
        "fact1": "Мне 30 лет",
        "fact2": "Живу в Челябинске",
        "fact3": "Учусь в GB с 07.08.2022",
    }

    context = {"facts": facts}
    return render(request, "myapp/about.html", context)
