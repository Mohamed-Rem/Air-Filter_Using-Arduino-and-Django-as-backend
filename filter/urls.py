from rest_framework import routers
from .views import FilterViewSet, SensorDataViewSet, TechnicianViewSet, FilterManualViewSet

router = routers.DefaultRouter()
router.register(r'filters', FilterViewSet)
router.register(r'sensordata', SensorDataViewSet)
router.register(r'technicians', TechnicianViewSet)
router.register(r'filtermanuals', FilterManualViewSet)

urlpatterns = router.urls
