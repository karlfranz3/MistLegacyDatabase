from .models import Location


def geojson_locations(request):
    return {'geojson_locations': Location.objects.all()}
