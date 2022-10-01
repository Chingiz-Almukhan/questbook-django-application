from django.shortcuts import render

from guestbook.forms import AddEditForm, SearchForm
from guestbook.models import GuestBook


def index_view(request):
    form = AddEditForm()
    search_form = SearchForm()
    guestbook = GuestBook.objects.filter(status='active').order_by('-created_at')
    context = {
        'guestbook': guestbook,
        'form': form,
        'search_form': search_form
    }
    return render(request, 'main.html', context)
