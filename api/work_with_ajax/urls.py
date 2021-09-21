from django.urls import path

from .views import todos, index, check_site_is_running, form_check


urlpatterns = [
    path('', index, name='index'),
    path('list_todos/', todos, name='list_todos'),

    path('check/', check_site_is_running, name='check'),
    path('form_check/', form_check, name='form_check'),
]