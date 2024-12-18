from rest_framework.views import APIView
from rest_framework.response import Response

from logistics.models import Package
from logistics.services.bin_packing_services.calculate_bin_packing_service import CalculateBinPackingService

class CalculateBinPackingView(APIView):
    def get(self, request, order_id):
        try:
            # OrderDetail'den package al
            packages = Package.objects.filter(order__id=order_id)

            # print(packages)
            CalculateBinPackingService.calculate_bin_packing(packages)
            
            return Response({"message": "Packages saved successfully!"}, status=200)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
    