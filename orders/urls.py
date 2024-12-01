from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, FileViewSet, OrderViewSet, OrderDetailViewSet, OrderResultViewSet

router = DefaultRouter()
router.register('companies', CompanyViewSet)
router.register('orders', OrderViewSet)
router.register('order-details', OrderDetailViewSet)
router.register('order-results', OrderResultViewSet)
router.register('files', FileViewSet)

urlpatterns = router.urls
