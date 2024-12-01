from rest_framework import serializers
from .models import Company, Order, OrderDetail, OrderResult

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

    class Meta:
        model = OrderDetail
        fields = '__all__'

class OrderResultSerializer(serializers.ModelSerializer):
    order = OrderSerializer()

    class Meta:
        model = OrderResult
        fields = '__all__'
