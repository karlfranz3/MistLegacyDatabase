from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django_datatables_view.base_datatable_view import BaseDatatableView

from front.models import Region


def regions(request):
    return render(request, 'regions.html', context={})


class RegionsWS(BaseDatatableView):
    model = Region
    columns = ['name', 'land', 'land_difficulty']
    order_columns = ['name', 'land', 'land_difficulty']

    def filter_queryset(self, qs):
        search = self.request.GET.get('search[value]', None)
        if search:
            search_parts = search.split(' ')
            qs_params = None
            for part in search_parts:
                q = Q(name__contains=part) | Q(land__name__contains=part) | Q(land_difficulty__contains=part)
                qs_params = qs_params & q if qs_params else q
            qs = qs.filter(qs_params)
        return qs
