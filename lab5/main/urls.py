from main.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', TaskViewSet, basename='task')
urlpatterns = router.urls