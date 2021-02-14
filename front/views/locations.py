from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django_datatables_view.base_datatable_view import BaseDatatableView

from front.models import Location


def locations(request):
    return render(request, 'locations.html', context={})


class LocationsWS(BaseDatatableView):
    model = Location
    columns = ['name', 'region', 'exploration']
    order_columns = ['name']

    def filter_queryset(self, qs):
        search = self.request.GET.get('search[value]', None)
        if search:
            search_parts = search.split(' ')
            qs_params = None
            for part in search_parts:
                q = Q(name__contains=part) | Q(region__name__contains=part) | Q(exploration__contains=part)
                qs_params = qs_params & q if qs_params else q
            qs = qs.filter(qs_params)
        return qs
