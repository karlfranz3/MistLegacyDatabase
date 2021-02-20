from django.shortcuts import render
from front.models import Location, Region


def map(request):
    locations = Location.objects.all()
    return render(request, 'map.html', context={'locations': locations})
