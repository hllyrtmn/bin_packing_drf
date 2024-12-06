from decimal import Decimal
import pandas as pd
from orders.models import Order, Company, Product, OrderDetail
from django.db import transaction
from datetime import datetime
from django.utils.timezone import now


class FileProcessingService:
    @staticmethod
    def process_file(file_instance):
        """
        Yüklenen dosyayı işle ve sipariş detaylarını oluştur.
        """
        # Dosya yolunu al
        file_path = file_instance.file.path

        # Excel dosyasını oku
        df = pd.read_excel(file_path, header=None)

        # B3 hücresindeki company bilgisi
        company_name = df.iloc[2, 1]

        # Şirketi bul veya oluştur
        company, created = Company.objects.get_or_create(company_name=company_name)

        # Dosyaya bağlı Order güncelle veya oluştur
        order = Order.objects.create(
            company=company,
            date=now(),
        )
        file_instance.order = order
        file_instance.save()

        # Ürün bilgilerini işle
        product_data = df.iloc[13:, [1, 2, 3, 4, 5]]  # 14. satırdan itibaren veriler
        FileProcessingService._process_products(order, product_data)

    @staticmethod
    def _process_products(order, product_data):
        """
        Verilen sipariş için ürün detaylarını işle ve kaydet.
        """
        
        for _, row in product_data.iterrows():
            product_type_code = row[2]
            product_type_type = str(row[1])
            width = Decimal(row[3])
            height = Decimal(row[4])
            count = int(row[5])
            # Ürünü bul
            product = Product.objects.filter(
                product_type__code=product_type_code,
                product_type__type=product_type_type,
                dimension__width=width,
                dimension__height=height
            ).first()

            if product:
                # OrderDetail oluştur
                OrderDetail.objects.create(
                    order=order,
                    product=product,
                    count=count  # Ürün adedi için bir varsayılan değer kullanılabilir veya dosyadan alınabilir
                )
            else:
                print(f"Eşleşen ürün bulunamadı: {row}")