from django.urls import path

from guestbook.views.base import index_view
from guestbook.views.add_view import add
from guestbook.views.edit_view import edit
from guestbook.views.delete_view import delete
from guestbook.views.search_view import search_view

urlpatterns = [
    path('', index_view, name='main'),
    path('add/', add, name='add'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('search/', search_view, name='search')

]
