from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.utils import translation
from django.urls import translate_url

from front.models import *


def set_lang(request, lang):
    redirect_to = translate_url(request.META['HTTP_REFERER'], lang)
    translation.activate(lang)
    response = HttpResponseRedirect(redirect_to=redirect_to)
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang)
    return response


def home(request):
    return render(request, 'home.html', context={})


def map(request):
    return render(request, 'map.html', context={})


def basics(request):
    lands = Land.objects.all()
    craftings = Crafting.objects.all()
    gatherings = Gathering.objects.all()
    adventures = Adventure.objects.all()
    weapons = Weapon.objects.all()
    reputations = Reputation.objects.all()
    companions = Companion.objects.all()
    guilds = Guild.objects.all()
    return render(request, 'basics.html',
                  context={'lands': lands, 'craftings': craftings, 'gatherings': gatherings, "companions": companions,
                           'adventures': adventures, 'weapons': weapons, 'reputations': reputations, 'guilds': guilds})


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
    return render(request, 'gathering.html', context={'gathering': gathering,
                                                      'books': books})


def weapon(request, pk):
    weapon = get_object_or_404(Weapon, pk=pk)
    recipes = Recipe.objects.filter(weapon=weapon)
    companions = Companion.objects.filter(weapon=weapon)
    return render(request, 'weapon.html', context={'weapon': weapon,
                                                   'recipes': recipes, 'companions': companions})


def reputation(request, pk):
    reputation = get_object_or_404(Reputation, pk=pk)
    recipes = Recipe.objects.filter(reputation=reputation)
    books = Book.objects.filter(reputation=reputation)
    spells = Spell.objects.filter(reputation=reputation)
    return render(request, 'reputation.html', context={'reputation': reputation,
                                                       'recipes': recipes, 'books': books, 'spells': spells})


def guild(request, pk):
    guild = get_object_or_404(Guild, pk=pk)
    spells = Spell.objects.filter(guild=guild)
    return render(request, 'guild.html', context={'guild': guild,
                                                  'spells': spells})


def regions(request):
    return render(request, 'regions.html', context={'regions': Region.objects.all()})


def locations(request):
    return render(request, 'locations.html', context={'locations': Location.objects.all()})


def books(request):
    return render(request, 'books.html', context={'books': Book.objects.all()})


def recipes(request):
    return render(request, 'recipes.html', context={'recipes': Recipe.objects.all()})


def spells(request):
    return render(request, 'spells.html', context={'spells': Spell.objects.all()})


def materials(request, material_type):
    return render(request, 'materials.html', context={'qs': Material.objects.filter(material_type__name_en__exact=material_type),
                                                      'material_type': material_type})


def ingredients(request, ingredient_type):
    return render(request, 'ingredients.html', context={'qs': Ingredient.objects.filter(ingredient_type__name_en__exact=ingredient_type),
                                                        'ingredient_type': ingredient_type})


def plants(request):
    return render(request, 'plants.html', context={'qs': Plant.objects.all()})
