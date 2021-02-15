from django.contrib import admin
from django.urls import path
from front.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),

    path('set_lang/<str:lang>', set_lang, name="set_lang"),
    path('search', search, name='search'),

    path('', home, name='home'),
    path('basics', basics, name='basics'),
    path('regions', regions, name='regions'),
    path("ws/regions", RegionsWS.as_view(), name="regions_ws"),
    path('locations', locations, name='locations'),
    path("ws/locations", LocationsWS.as_view(), name="locations_ws"),
    path('books', books, name='books'),
    path("ws/books", BooksWS.as_view(), name="books_ws"),
    path('recipes', recipes, name='recipes'),
    path("ws/recipes", RecipesWS.as_view(), name="recipes_ws"),
    path('spells', spells, name='spells'),
    path("ws/spells", SpellsWS.as_view(), name="spells_ws"),

    path('land/<int:pk>', land, name='land'),
    path('adventure/<int:pk>', adventure, name='adventure'),
    path('crafting/<int:pk>', crafting, name='crafting'),
    path('gathering/<int:pk>', gathering, name='gathering'),
    path('weapon/<int:pk>', weapon, name='weapon'),
    path('reputation/<int:pk>', reputation, name='reputation'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
