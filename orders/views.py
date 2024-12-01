from rest_framework.viewsets import ModelViewSet
from .models import Company, File, Order, OrderDetail, OrderResult
from .serializers import CompanySerializer, FileSerializer, OrderSerializer, OrderDetailSerializer, OrderResultSerializer

class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetailViewSet(ModelViewSet):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer

class OrderResultViewSet(ModelViewSet):
    queryset = OrderResult.objects.all()
    serializer_class = OrderResultSerializer

class FileViewSet(ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer