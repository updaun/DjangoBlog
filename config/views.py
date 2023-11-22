from django.http.response import HttpResponse, JsonResponse
import random
from django.views import View
from django.shortcuts import render


def helloworld(request):
    return HttpResponse("<h1>Hello World</h1>")

def helloworld_json(request):
    return JsonResponse({"message":"Hello World"})

def random_number(request):
    random_number = random.randint(1, 10000)
    return HttpResponse(f"<h1>Random Number: {random_number}</h1>")


class HomeView(View):
    def get(self, request):
        return render(request, "home.html")
    