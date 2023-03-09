from rest_framework.routers import DefaultRouter
from authentication.views import AuthToken

router = DefaultRouter()
router.register("token_auth", AuthToken, basename="token_auth")

urlpatterns = router.urls


# import pprint
# pprint.pprint(router.get_urls())