from django.urls import path
from rest_framework import routers
from .views import UniversityViewSet, StudentViewSet, index, students


router = routers.DefaultRouter()
router.register("university", UniversityViewSet, basename='uni')
router.register("students", StudentViewSet)

urlpatterns = [
    path('index/', index, name='index'),
    path('show_students/', students, name='show_students')
]

urlpatterns += router.urls
