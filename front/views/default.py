from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.utils import translation
from django.urls import translate_url
from django.core.cache import cache
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.views.decorators.cache import never_cache

from front.models import *


def set_lang(request, lang):
    redirect_to = translate_url(request.META['HTTP_REFERER'], lang)
    translation.activate(lang)
    response = HttpResponseRedirect(redirect_to=redirect_to)
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang)
    return response


@never_cache
def clear_cache(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    cache.clear()
    return HttpResponse('Cache has been cleared')


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
    books = Book.objects.filter(land=land).order_by('reputation', 'guild', 'reputation_guild_value')
    regions = Region.objects.filter(land=land).order_by('-land_difficulty')
    companions = CompanionSkill.objects.filter(land=land).order_by('-bonus')
    return render(request, 'land.html', context={'land': land, 'companions': companions,
                                                 'regions': regions, 'books': books})


def adventure(request, pk):
    adventure = get_object_or_404(Adventure, pk=pk)
    trainings = Training.objects.filter(adventure=adventure).order_by('-difficulty')
    books = Book.objects.filter(adventure=adventure).order_by('reputation', 'guild', 'reputation_guild_value')
    flagsteps = BlueFlagsStep.objects.filter(adventure=adventure).order_by('-difficulty')
    companions = CompanionSkill.objects.filter(adventure=adventure).order_by('-bonus')
    return render(request, 'adventure.html', context={'adventure': adventure, 'trainings': trainings, 'companions': companions,
                                                      'books': books, 'flagsteps': flagsteps})


def crafting(request, pk):
    crafting = get_object_or_404(Crafting, pk=pk)
    books = Book.objects.filter(crafting=crafting).order_by('reputation', 'guild', 'reputation_guild_value')
    companions = CompanionSkill.objects.filter(crafting=crafting).order_by('-bonus')
    return render(request, 'crafting.html', context={'crafting': crafting, 'companions': companions,
                                                     'books': books})


def gathering(request, pk):
    gathering = get_object_or_404(Gathering, pk=pk)
    books = Book.objects.filter(gathering=gathering).order_by('reputation', 'guild', 'reputation_guild_value')
    flagsteps = BlueFlagsStep.objects.filter(gathering=gathering).order_by('-difficulty')
    companions = CompanionSkill.objects.filter(gathering=gathering).order_by('-bonus')
    return render(request, 'gathering.html', context={'gathering': gathering, 'flagsteps': flagsteps, 'companions': companions,
                                                      'books': books})


def weapon(request, pk):
    weapon = get_object_or_404(Weapon, pk=pk)
    recipes = Recipe.objects.filter(weapon=weapon).order_by('reputation', 'guild', 'reputation_guild_value')
    companions = Companion.objects.filter(weapon=weapon)
    flagsteps = BlueFlagsStep.objects.filter(weapon=weapon).order_by('-difficulty')
    return render(request, 'weapon.html', context={'weapon': weapon, 'flagsteps': flagsteps,
                                                   'recipes': recipes, 'companions': companions})


def reputation(request, pk):
    reputation = get_object_or_404(Reputation, pk=pk)
    recipes = Recipe.objects.filter(reputation=reputation).order_by('reputation', 'guild', 'reputation_guild_value')
    books = Book.objects.filter(reputation=reputation).order_by('reputation', 'guild', 'reputation_guild_value')
    talents = Talent.objects.filter(reputation=reputation).order_by('reputation', 'guild', 'reputation_guild_value')
    return render(request, 'reputation.html', context={'reputation': reputation,
                                                       'recipes': recipes, 'books': books, 'talents': talents})


def guild(request, pk):
    guild = get_object_or_404(Guild, pk=pk)
    recipes = Recipe.objects.filter(guild=guild).order_by('reputation', 'guild', 'reputation_guild_value')
    talents = Talent.objects.filter(guild=guild).order_by('reputation', 'guild', 'reputation_guild_value')
    return render(request, 'guild.html', context={'guild': guild, 'recipes': recipes,
                                                  'talents': talents})


def regions(request):
    return render(request, 'regions.html', context={'regions': Region.objects.all()})


def locations(request):
    return render(request, 'locations.html', context={'locations': Location.objects.all()})


def books(request):
    return render(request, 'books.html', context={'books': Book.objects.all()})


def recipes(request):
    return render(request, 'recipes.html', context={'recipes': Recipe.objects.all()})


def talents(request):
    return render(request, 'talents.html', context={'talents': Talent.objects.all()})


def materials(request, material_type):
    return render(request, 'materials.html', context={'qs': Material.objects.filter(material_type__name_en__exact=material_type),
                                                      'material_type': material_type})


def components(request, component_type):
    return render(request, 'components.html', context={'qs': Component.objects.filter(component_type__name_en__exact=component_type),
                                                       'component_type': component_type})


def plants(request):
    return render(request, 'plants.html', context={'qs': Plant.objects.all()})


def flags(request):
    return render(request, 'flags.html', context={'qs': BlueFlags.objects.all()})


def monsters(request):
    return render(request, 'todo.html', context={'qs': Plant.objects.all()})


def guides(request):
    return render(request, 'guides.html', context={'guides': Guide.objects.all()})


def companions(request):
    return render(request, 'companion.html', context={'companions': Companion.objects.all()})
