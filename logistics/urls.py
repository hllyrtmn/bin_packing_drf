from rest_framework.routers import DefaultRouter
from .views import PalletViewSet, PackageViewSet, PackageDetailViewSet

router = DefaultRouter()
router.register('pallets', PalletViewSet)
router.register('packages', PackageViewSet)
router.register('package-details', PackageDetailViewSet)

urlpatterns = router.urls
