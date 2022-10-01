from django.shortcuts import render

from guestbook.models import GuestBook


# Create your views here.
def index_view(request):
    guestbook = GuestBook.objects.filter(status='active').order_by('-created_at')
    context = {
        'guestbook': guestbook
    }
    return render(request, 'main.html', context)
