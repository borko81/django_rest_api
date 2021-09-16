from django.urls import path
from .views import HelloView


urlpatterns = [
    path('hello_view/', HelloView.as_view()),
]