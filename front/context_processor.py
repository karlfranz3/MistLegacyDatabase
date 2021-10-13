from .models import Location, Region, BlueFlags, Elixir


def geojson_locations(request):
    return {'geojson_locations': Location.objects.all()}


def geojson_regions(request):
    return {'geojson_regions': Region.objects.all()}


def geojson_blueflags(request):
    return {'geojson_blueflags': BlueFlags.objects.all()}


def geojson_elixirs(request):
    return {'geojson_elixirs': Elixir.objects.all()}
