
from django.http.response import HttpResponse, JsonResponse
import random

def helloworld(request):
    return HttpResponse("<h1>HelloWorld</h1>")

def helloworld_json(request):
    return JsonResponse({'message': 'Hello World'})

def random_number(request):
    random_number = random.randint(0, 10000)
    return HttpResponse(f"<h1>Random Number {random_number}</h1>")