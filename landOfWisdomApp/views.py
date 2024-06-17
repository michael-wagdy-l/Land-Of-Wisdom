import json

from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.shortcuts import render
from landOfWisdomApp.Orion import Orion


# Create your views here.
def orion(request):
    if request.method == 'POST':
        print(request.POST.get('userInput'))
    return render(request, 'orion.html')


def chatbot(request):
    if request.method == 'POST':
        try:
            # Parse the JSON data from the request body
            data = json.loads(request.body)
            # Extract the 'message' field from the JSON data
            message = data.get('message')
            orion = Orion()
            response = orion.take_message(message)
        except json.JSONDecodeError:
            return HttpResponseBadRequest('Invalid JSON data')

    return JsonResponse(response, status=200)
