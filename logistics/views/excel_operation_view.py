from rest_framework.views import APIView
from rest_framework.response import Response

from logistics.models import Package
from logistics.services.excel_operation_services.settlement_service import SettlementService

class ExcelOperationView(APIView):
    def get(self, request, order_id):
        try:
            # OrderDetail'den package al
            packages = Package.objects.filter(order__id=order_id)

            # print(packages)
            SettlementService.create_settlement_report(packages)
            
            return Response({"message": "Excel Report Created!"}, status=200)
        except Exception as e:
            return Response({"error": str(e)}, status=500)