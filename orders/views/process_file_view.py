from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from orders.models import File
from orders.services.file_processing_service import FileProcessingService

class ProcessFileView(APIView):
    """
    Yüklenen dosyayı işleyen API.
    """

    def post(self, request, file_id):
        try:
            file_instance = File.objects.get(id=file_id)

            # Dosyayı işle
            FileProcessingService.process_file(file_instance)

            return Response({"message": "File processed successfully!"}, status=status.HTTP_200_OK)
        except File.DoesNotExist:
            return Response({"error": "File not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)