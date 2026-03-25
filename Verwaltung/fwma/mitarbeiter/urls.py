from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import UserViewSet, MitarbeiterViewSet

router = DefaultRouter()
router.register(r'mitarbeiter', MitarbeiterViewSet) 
router.register(r'users', UserViewSet)

urlpatterns = router.urls  