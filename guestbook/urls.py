from django.urls import path

from guestbook.views import index_view, edit, delete

urlpatterns = [
    path('', index_view, name='main'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('delete/<int:pk>/', delete, name='delete'),

]