from django.shortcuts import render
from django.db.models import Sum
from front.models import *


def jenniel1(request):
    materials = GatheringPoint.objects.exclude(material__isnull=True).values_list('material__name', 'number').values('material__name').order_by('material__name').annotate(total=Sum('number'))
    plants = GatheringPoint.objects.exclude(plant__isnull=True).values_list('plant__name', 'number').values('plant__name').order_by('plant__name').annotate(total=Sum('number'))
    return render(request, 'jenniel1.html', context={'materials': materials, 'plants': plants})
