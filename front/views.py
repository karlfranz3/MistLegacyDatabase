from django.shortcuts import render

from .models import Training


def home(request):
    trainings = Training.objects.all()
    return render(request, 'home.html', context={'trainings': trainings})


def basics(request):
    return render(request, 'basics.html', context={})


def search(request):
    return render(request, 'search.html', context={})


