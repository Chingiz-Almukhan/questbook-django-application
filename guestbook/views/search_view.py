from django.shortcuts import render

from guestbook.forms import SearchForm, AddEditForm
from guestbook.models import GuestBook


def search_view(request):
    guestbook = GuestBook.objects.filter(status='active').order_by('-created_at')
    form = SearchForm(data=request.POST)
    add_form = AddEditForm()
    if form.is_valid():
        search_result = request.POST.get('search')
        guestbook = GuestBook.objects.filter(author=search_result).order_by('-created_at')
        search_form = SearchForm()
        context = {
            'guestbook': guestbook,
            'form': add_form,
            'search_form': search_form
        }
        return render(request, 'main.html', context)
    else:
        return render(request, 'main.html', context={'form': add_form, 'guest': guestbook, 'search_form': form})
