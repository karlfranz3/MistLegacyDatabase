from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.utils import translation
from django.views.generic import DetailView

from .models import Weapon, Land, Crafting, Gathering, Adventure, Reputation, EquipmentSlot, Region, Location, Book, Training, Recipe


def set_lang(request, lang):
    translation.activate(lang)
    response = HttpResponseRedirect(redirect_to=request.META['HTTP_REFERER'])
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang)
    return response


def home(request):
    return render(request, 'home.html', context={})


def basics(request):
    lands = Land.objects.all()
    craftings = Crafting.objects.all()
    gatherings = Gathering.objects.all()
    adventures = Adventure.objects.all()
    weapons = Weapon.objects.all()
    reputations = Reputation.objects.all()
    return render(request, 'basics.html',
                  context={'lands': lands, 'craftings': craftings, 'gatherings': gatherings,
                           'adventures': adventures, 'weapons': weapons, 'reputations': reputations})


def regions(request):
    regions = Region.objects.all()
    return render(request, 'basics.html', context={'regions': regions})


def locations(request):
    locations = Location.objects.all()
    return render(request, 'basics.html', context={'locations': locations})


def search(request):
    return render(request, 'search.html', context={})


def land(request, pk):
    land = get_object_or_404(Land, pk=pk)
    books = Book.objects.filter(land=land)
    regions = Region.objects.filter(land=land)
    return render(request, 'land.html', context={'land': land,
                                                 'regions': regions, 'books': books})


def adventure(request, pk):
    adventure = get_object_or_404(Adventure, pk=pk)
    trainings = Training.objects.filter(adventure=adventure)
    books = Book.objects.filter(adventure=adventure)
    return render(request, 'adventure.html', context={'adventure': adventure,
                                                      'trainings': trainings, 'books': books})


def crafting(request, pk):
    crafting = get_object_or_404(Crafting, pk=pk)
    books = Book.objects.filter(crafting=crafting)
    return render(request, 'crafting.html', context={'crafting': crafting,
                                                     'books': books})


def gathering(request, pk):
    gathering = get_object_or_404(Gathering, pk=pk)
    books = Book.objects.filter(gathering=gathering)
    return render(request, 'crafting.html', context={'gathering': gathering,
                                                     'books': books})


def weapon(request, pk):
    weapon = get_object_or_404(Weapon, pk=pk)
    recipes = Recipe.objects.filter(weapon=weapon)
    return render(request, 'crafting.html', context={'weapon': weapon,
                                                     'recipes': recipes})


def reputation(request, pk):
    reputation = get_object_or_404(Reputation, pk=pk)
    recipes = Recipe.objects.filter(reputation=reputation)
    books = Book.objects.filter(reputation=reputation)
    return render(request, 'reputation.html', context={'reputation': reputation,
                                                      'recipes': recipes, 'books': books})
