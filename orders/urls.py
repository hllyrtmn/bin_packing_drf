from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, OrderViewSet, OrderDetailViewSet, OrderResultViewSet

router = DefaultRouter()
router.register('companies', CompanyViewSet)
router.register('orders', OrderViewSet)
router.register('order-details', OrderDetailViewSet)
router.register('order-results', OrderResultViewSet)

urlpatterns = router.urls
