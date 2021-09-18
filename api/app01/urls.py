from rest_framework import routers
from .views import UniversityViewSet, StudentViewSet


router = routers.DefaultRouter()
router.register("university", UniversityViewSet)
router.register("students", StudentViewSet)


urlpatterns = router.urls
