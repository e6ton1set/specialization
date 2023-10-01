from django.http import HttpResponse
from django.views import View


def hello(request):
    return HttpResponse("It's view-function!")


class HelloView(View):
    @staticmethod
    def get(request):
        return HttpResponse("It's view-Class")