from rest_framework.routers import SimpleRouter
from .views import UrlCheckerViewSet

app_name = 'api'

router = SimpleRouter()
router.register('url_lists', UrlCheckerViewSet)

urlpatterns = [
    ] + router.urls
