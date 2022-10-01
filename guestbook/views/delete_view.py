from django.shortcuts import redirect

from guestbook.models import GuestBook


def delete(request, pk):
    guest = GuestBook.objects.get(pk=pk)
    guest.delete()
    return redirect('main')
