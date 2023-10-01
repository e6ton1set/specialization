from django.shortcuts import render


def index(request):
    context = {}
    return render(request, "myapp2/index.html", context)