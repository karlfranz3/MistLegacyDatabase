from .models import Location, Region


def geojson_locations(request):
    return {'geojson_locations': Location.objects.all()}


def geojson_regions(request):
    return {'geojson_regions': Region.objects.all()}
