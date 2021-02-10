from django.shortcuts import render

from .models import Training


def test(request):
    trainings = Training.objects.all()
    return render(request, 'test.html', context={'trainings': trainings})
