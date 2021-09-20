from django.urls import path

from .views import todos, index


urlpatterns = [
    path('', index, name='index'),
    path('list_todos/', todos, name='list_todos'),
]