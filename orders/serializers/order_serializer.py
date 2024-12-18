from core.serializers import BaseTrackingSerializer
from orders.models import Order,OrderDetail,Company,OrderResult
from products.serializers import ProductSerializer

class CompanySerializer(BaseTrackingSerializer):
    class Meta:
        model = Company
        fields = ['company_name','country']
        
class OrderSerializer(BaseTrackingSerializer):
    company = CompanySerializer()

    class Meta:
        model = Order
        fields = ['company','date']
        
class OrderDetailSerializer(BaseTrackingSerializer):
    order = OrderSerializer()
    product = ProductSerializer()
    
    class Meta:
        model = OrderDetail
        fields = ['order','product','count','unit_price']

class OrderResultSerializer(BaseTrackingSerializer):
    order = OrderSerializer()

    class Meta:
        model = OrderResult
        fields = ['order','result']


