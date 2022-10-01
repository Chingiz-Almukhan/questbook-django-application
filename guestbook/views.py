from django.shortcuts import render, redirect

from guestbook.forms import AddEditForm
from guestbook.models import GuestBook


# Create your views here.
def index_view(request):
    form = AddEditForm()
    guestbook = GuestBook.objects.filter(status='active').order_by('-created_at')
    context = {
        'guestbook': guestbook,
        'form': form
    }
    if request.method == 'POST':
        form = AddEditForm(data=request.POST)
        if form.is_valid():
            create = GuestBook.objects.create(author=form.cleaned_data['author'],
                                              email=form.cleaned_data["email"], text=form.cleaned_data['text'])
            return redirect('main')
        else:
            return render(request, 'main.html', context={'form': form,
                                                         'guestbook': guestbook})
    return render(request, 'main.html', context)


def edit(request, pk):
    guest = GuestBook.objects.get(pk=pk)
    if request.method == 'GET':
        form = AddEditForm(initial={
            'author': guest.author,
            'email': guest.email,
            'text': guest.text

        })
        return render(request, 'edit.html', context={'form': form, 'guest': guest})
    elif request.method == 'POST':
        form = AddEditForm(data=request.POST)
        if form.is_valid():
            guest.author = form.cleaned_data['author']
            guest.email = form.cleaned_data["email"]
            guest.text = form.cleaned_data['text']
            guest.save()
            return redirect('main')
        else:
            return render(request, 'edit.html', context={'form': form, 'guest': guest})


def delete(request, pk):
    guest = GuestBook.objects.get(pk=pk)
    guest.delete()
    return redirect('main')
