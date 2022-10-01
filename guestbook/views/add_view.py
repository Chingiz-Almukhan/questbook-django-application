from django.shortcuts import redirect, render

from guestbook.forms import AddEditForm, SearchForm
from guestbook.models import GuestBook


def add(request):
    guestbook = GuestBook.objects.filter(status='active').order_by('-created_at')
    form = AddEditForm(data=request.POST)
    search_form = SearchForm()
    if form.is_valid():
        create = GuestBook.objects.create(author=form.cleaned_data['author'],
                                          email=form.cleaned_data["email"], text=form.cleaned_data['text'])
        return redirect('main')
    else:
        return render(request, 'main.html', context={'form': form,
                                                     'guestbook': guestbook,
                                                     'search_form': search_form})
