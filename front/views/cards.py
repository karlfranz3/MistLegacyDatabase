from django.shortcuts import render, get_object_or_404

from front.models import *


def companion_card(request, pk):
    companion = get_object_or_404(Companion, pk=pk)
    return render(request, 'companion_card.html', context={'companion': companion})


def book_card(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book_card.html', context={'book': book})


def talent_card(request, pk):
    talent = get_object_or_404(Talent, pk=pk)
    return render(request, 'talent_card.html', context={'talent': talent})


def recipe_card(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipe_card.html', context={'recipe': recipe})
