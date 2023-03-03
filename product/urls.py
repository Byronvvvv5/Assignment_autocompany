from rest_framework.routers import DefaultRouter
from product.views import ProductViewSet, ProductDetailViewSet

router = DefaultRouter()
router.register("products", ProductViewSet, basename="products")
router.register("detail", ProductDetailViewSet, basename="detail")

urlpatterns = router.urls