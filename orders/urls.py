from django.urls import include, path
from rest_framework.routers import DefaultRouter

from orders.views import CompanyViewSet, FileViewSet, OrderViewSet, OrderDetailViewSet, OrderResultViewSet,ProcessFileView

router = DefaultRouter()
router.register('companies', CompanyViewSet)
router.register('orders', OrderViewSet)
router.register('order-details', OrderDetailViewSet)
router.register('order-results', OrderResultViewSet)
router.register(r'files', FileViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('process-file/<uuid:file_id>/', ProcessFileView.as_view(), name='process-file'),
]
