from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django_datatables_view.base_datatable_view import BaseDatatableView

from front.models import Recipe


def recipes(request):
    return render(request, 'recipes.html', context={})


class RecipesWS(BaseDatatableView):
    model = Recipe
    columns = ['name', 'location', 'npc', 'reputation', 'reputation_guild_value', 'price', 'building', 'equipment_slot', 'weapon', 'daytime']
    order_columns = ['name', 'location', 'npc', 'reputation', 'reputation_guild_value', 'price', 'building', 'equipment_slot', 'weapon', 'daytime']

    def filter_queryset(self, qs):
        search = self.request.GET.get('search[value]', None)
        if search:
            search_parts = search.split(' ')
            qs_params = None
            for part in search_parts:
                q = Q(price__contains=part) | Q(reputation__name__contains=part) | Q(npc__name__contains=part)
                qs_params = qs_params & q if qs_params else q
            qs = qs.filter(qs_params)
        return qs
