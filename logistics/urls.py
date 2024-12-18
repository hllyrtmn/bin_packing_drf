from django.urls import include, path
from rest_framework.routers import DefaultRouter

from logistics.views.calculate_bin_packing_view import CalculateBinPackingView
from .views import PalletViewSet, PackageViewSet, PackageDetailViewSet,TruckViewSet
from logistics.views.calculate_package_view import CalculatePackageView

router = DefaultRouter()
router.register('pallets', PalletViewSet)
router.register('packages', PackageViewSet)
router.register('package-details', PackageDetailViewSet)
router.register('trucks',TruckViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('calculate-packing/<uuid:order_id>/', CalculateBinPackingView.as_view(), name='calculate-packing'),
    path('calculate-box/<uuid:order_id>/', CalculatePackageView.as_view(), name='calculate-box')
]