from django.urls import path, include
from .views import HelloView, HelloViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('hello_sets', HelloViewSet, basename='hello_sets')

urlpatterns = [
    path('hello_view/', HelloView.as_view()),
    path('', include(router.urls))
]
