from django.shortcuts import render, get_object_or_404

from front.models import *


def companion_card(request, pk):
    companion = get_object_or_404(Companion, pk=pk)
    return render(request, 'companion_card.html', context={'companion': companion})


def region_card(request, pk):
    region = get_object_or_404(Region, pk=pk)
    return render(request, 'region_card.html', context={'region': region})


def location_card(request, pk):
    location = get_object_or_404(Location, pk=pk)
    return render(request, 'location_card.html', context={'location': location})


def book_card(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book_card.html', context={'book': book})


def spell_card(request, pk):
    spell = get_object_or_404(Spell, pk=pk)
    return render(request, 'spell_card.html', context={'spell': spell})


def recipe_card(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipe_card.html', context={'recipe': recipe})
