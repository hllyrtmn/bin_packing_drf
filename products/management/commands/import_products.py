import os
from products.models import Product, ProductType, Dimension, WeightType
import json
from django.conf import settings

file_path = os.path.join(settings.BASE_DIR, 'data', 'products.json')
with open(file_path, 'r', encoding='utf-8') as file:
    products = json.load(file)

def add_products_to_db(products):
    for product_data in products:
        # Product Type
        product_type_data = product_data['product_type']
        product_type, _ = ProductType.objects.get_or_create(
            code=product_type_data['code'],
            type=product_type_data['type'],
            is_deleted=product_type_data['is_deleted'],
            deleted_time=product_type_data['deleted_time']
        )

        # Dimension
        dimension_data = product_data['dimension']
        dimension, _ = Dimension.objects.get_or_create(
            width=dimension_data['width'],
            height=dimension_data['height'],
            depth=dimension_data['depth'],
            unit=dimension_data['unit'],
            is_deleted=dimension_data['is_deleted'],
            deleted_time=dimension_data['deleted_time']
        )

        # Weight Type
        weight_type_data = product_data['weight_type']
        weight_type, _ = WeightType.objects.get_or_create(
            std=weight_type_data['std'],
            eco=weight_type_data['eco'],
            pre=weight_type_data['pre'],
            is_deleted=weight_type_data['is_deleted'],
            deleted_time=weight_type_data['deleted_time']
        )

        # Product
        Product.objects.create(
            product_type=product_type,
            dimension=dimension,
            weight_type=weight_type,
            is_deleted=product_data['is_deleted'],
            deleted_time=product_data['deleted_time']
        )

# JSON'dan veritabanına ürün ekle
add_products_to_db(products)