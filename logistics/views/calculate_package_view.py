from rest_framework.views import APIView
from rest_framework.response import Response
from orders.models import OrderDetail
from logistics.models import Pallet
from logistics.services.calculate_package_service import CalculatePackageService

class CalculatePackageView(APIView):
    def get(self, request, order_id):
        try:
            # OrderDetail'den ürünleri al
            order_details = OrderDetail.objects.filter(order__id=order_id)

            # Pallet'leri al
            pallets = Pallet.objects.all()
            
            # Hesaplamayı yap
            packages = CalculatePackageService.create_packages(order_details, pallets)
            CalculatePackageService.save_packages_and_details_to_db(packages,order_id)
            # Sonuçları döndür
            return Response({"message": "Packages saved successfully!"}, status=200)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
    