from rest_framework.routers import SimpleRouter
from .views import UrlCheckerViewSet

app_name = 'api'

router = SimpleRouter()
router.register('urls', UrlCheckerViewSet)

urlpatterns = [
    ] + router.urls
