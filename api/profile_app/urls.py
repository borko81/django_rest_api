from django.urls import path, include
from .views import HelloView, HelloViewSet, UserLoginApiView, UserProfileViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('hello_sets', HelloViewSet, basename='hello_sets')
router.register('user_info', UserProfileViewSet, basename='userinfo')

urlpatterns = [
    path('hello_view/', HelloView.as_view()),
    path('login/', UserLoginApiView.as_view()),
    path('', include(router.urls))
]
