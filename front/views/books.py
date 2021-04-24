from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django_datatables_view.base_datatable_view import BaseDatatableView

from front.models import Book


def books(request):
    return render(request, 'books.html', context={})


class BooksWS(BaseDatatableView):
    model = Book
    columns = ['value', 'location', 'npc', 'reputation', 'reputation_guild_value', 'price', 'count', 'daytime']
    order_columns = ['value', 'location', 'npc', 'reputation', 'reputation_guild_value', 'price', 'count', 'daytime']

    def render_column(self, row, column):
        # We want to render user as a custom column
        if column == 'value':
            # escape HTML for security reasons
            return row.__str__()
        else:
            return super(BooksWS, self).render_column(row, column)

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
