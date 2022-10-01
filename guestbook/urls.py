from django.urls import path

from views.base import index_view
from views.add_view import add
from views.edit_view import edit
from views.delete_view import delete
from views.search_view import search_view

urlpatterns = [
    path('', index_view, name='main'),
    path('add/', add, name='add'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('search/', search_view, name='search')

]
