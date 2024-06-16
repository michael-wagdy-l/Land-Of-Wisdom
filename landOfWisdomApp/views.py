from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from landOfWisdomApp.Orion import Orion


# Create your views here.
def orion(request):
    if request.method == 'POST':
        print(request.POST.get('userInput'))
    return render(request, 'orion.html')


def chatbot(request):
    orion = Orion()
    response = orion.take_message(request.POST.get("user-input"))

    return JsonResponse(response, status=200)
