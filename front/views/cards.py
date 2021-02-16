from django.shortcuts import render, get_object_or_404

from front.models import Companion


def companion_card(request, pk):
    companion = get_object_or_404(Companion, pk=pk)
    return render(request, 'companion_light.html', context={'companion': companion})
