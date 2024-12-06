from rest_framework import serializers
from orders.models import Order,OrderDetail,Company,OrderResult
from products.serializers import ProductSerializer

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
        
class OrderSerializer(serializers.ModelSerializer):
    company = CompanySerializer()

    class Meta:
        model = Order
        fields = '__all__'
        
class OrderDetailSerializer(serializers.ModelSerializer):
    order = OrderSerializer()
    product = ProductSerializer()
    
    class Meta:
        model = OrderDetail
        fields = '__all__'

class OrderResultSerializer(serializers.ModelSerializer):
    order = OrderSerializer()

    class Meta:
        model = OrderResult
        fields = '__all__'


