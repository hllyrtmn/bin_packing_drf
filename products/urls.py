from rest_framework.routers import DefaultRouter
from .views import ProductTypeViewSet, DimensionViewSet, WeightTypeViewSet, ProductViewSet

router = DefaultRouter()
router.register('product-types', ProductTypeViewSet)
router.register('dimensions', DimensionViewSet)
router.register('weight-types', WeightTypeViewSet)
router.register('products', ProductViewSet)

urlpatterns = router.urls
