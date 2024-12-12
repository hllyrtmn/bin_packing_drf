from rest_framework import serializers
from orders.models import Order,OrderDetail,Company,OrderResult
from products.serializers import ProductSerializer

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['company_name','country']
        
class OrderSerializer(serializers.ModelSerializer):
    company = CompanySerializer()

    class Meta:
        model = Order
        fields = ['company','date']
        
class OrderDetailSerializer(serializers.ModelSerializer):
    order = OrderSerializer()
    product = ProductSerializer()
    
    class Meta:
        model = OrderDetail
        fields = ['order','product','count','unit_price']

class OrderResultSerializer(serializers.ModelSerializer):
    order = OrderSerializer()

    class Meta:
        model = OrderResult
        fields = ['order','result']


