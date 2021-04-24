from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django_datatables_view.base_datatable_view import BaseDatatableView

from front.models import Spell


def spells(request):
    return render(request, 'spells.html', context={})


class SpellsWS(BaseDatatableView):
    model = Spell
    columns = ['name', 'level', 'location', 'npc', 'reputation', 'guild', 'reputation_guild_value', 'price', 'daytime']
    order_columns = ['name', 'level', 'location', 'npc', 'reputation', 'guild', 'reputation_guild_value', 'price', 'daytime']

    def filter_queryset(self, qs):
        search = self.request.GET.get('search[value]', None)
        if search:
            search_parts = search.split(' ')
            qs_params = None
            for part in search_parts:
                q = Q(name__contains=part) | Q(reputation__name__contains=part) | Q(npc__name__contains=part) | Q(location__name__contains=part)
                qs_params = qs_params & q if qs_params else q
            qs = qs.filter(qs_params)
        return qs
