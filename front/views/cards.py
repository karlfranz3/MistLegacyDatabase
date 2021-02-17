from django.shortcuts import render, get_object_or_404

from front.models import Companion, Region


def companion_card(request, pk):
    companion = get_object_or_404(Companion, pk=pk)
    return render(request, 'companion_card.html', context={'companion': companion})


def region_card(request, pk):
    region = get_object_or_404(Region, pk=pk)
    return render(request, 'region_card.html', context={'region': region})
