from .models import Location, Region, BlueFlags


def geojson_locations(request):
    return {'geojson_locations': Location.objects.all()}


def geojson_regions(request):
    return {'geojson_regions': Region.objects.all()}


def geojson_blueflags(request):
    return {'geojson_blueflags': BlueFlags.objects.all()}
