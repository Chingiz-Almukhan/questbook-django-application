from django.urls import path

from guestbook.views import index_view, edit, delete, add, search_view

urlpatterns = [
    path('', index_view, name='main'),
    path('add/', add, name='add'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('search/', search_view, name='search')

]