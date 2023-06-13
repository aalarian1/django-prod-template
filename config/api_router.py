from django.conf import settings
from whatto.eat.views import BusinessViewSet
from rest_framework.routers import DefaultRouter, SimpleRouter

from whatto.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("Business", BusinessViewSet)


app_name = "api"
urlpatterns = router.urls
