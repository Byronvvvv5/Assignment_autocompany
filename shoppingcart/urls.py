from rest_framework.routers import DefaultRouter
from shoppingcart.views import ShoppingCartViewSet

router = DefaultRouter()
router.register("shoppingcart", ShoppingCartViewSet, basename="shoppingcart")


urlpatterns = router.urls