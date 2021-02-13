from django.shortcuts import render, redirect
from django.utils import translation

from .models import Training, Region


def set_lang(request, lang):
    translation.activate(lang)
    return redirect(home)


def home(request):
    if request.method == 'POST':
        lang = request.POST['language']
        translation.activate(lang)

    regions = Region.objects.all()
    return render(request, 'home.html', context={'regions': regions})


def basics(request):
    return render(request, 'basics.html', context={})


def search(request):
    return render(request, 'search.html', context={})


