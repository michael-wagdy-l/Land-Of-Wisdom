from django.shortcuts import render

# Create your views here.
def orion(request):
    return render(request, 'orion.html')