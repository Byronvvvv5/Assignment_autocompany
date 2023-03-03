from rest_framework.routers import DefaultRouter
from order.views import OrderViewSet
router = DefaultRouter()
router.register("delivery", OrderViewSet, basename="delivery")

urlpatterns = router.urls