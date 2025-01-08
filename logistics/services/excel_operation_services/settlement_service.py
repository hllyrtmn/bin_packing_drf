from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, Border, Side
from openpyxl.utils import get_column_letter

from logistics.models import PackageDetail

class SettlementService:
    @staticmethod
    def create_settlement_report(packages):
        wb = Workbook()
        ws = wb.active
        column_names = [
            "No", "Palet Genişlik", "X", "Palet Derinlik", "KOD1", "KOD", "KALAN",
            "Ürün Kodu", "Mod", "Panel Boyu", "Dikey Sıra Adedi","Kat Adedi(Dikey)" ,"Yatay Sıra Adedi",
            "Kat Adedi(Yatay)", "Eşdeğer", "Ara Toplam", "Palet Adet",
            "Metre", "Birim Ağırlık", "Net", "Palet Ağırlık", "Toplam"
        ]
        
        # Kenarlık tanımları
        thin_border = Border(
            left=Side(style="thin"),
            right=Side(style="thin"),
            top=Side(style="thin"),
            bottom=Side(style="thin")
        )
        
        # Başlık satırı
        for col_num, col_name in enumerate(column_names, 1):
            cell = ws.cell(row=1, column=col_num, value=col_name)
            cell.font = Font(bold=True)
            cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
            cell.border = thin_border  # Başlıklara kenarlık ekle
        
        # Filtreyi ilk satırda ekle
        ws.auto_filter.ref = f"A1:{get_column_letter(len(column_names))}1"

        row_num = 2  # Veri satırları 2. satırdan başlar
        col_widths = [len(col_name) for col_name in column_names]  # Sütun genişlikleri için başlık uzunluklarını başlangıç değeri olarak alıyoruz
        
        for package in packages:
            package_details = PackageDetail.objects.filter(package_id=package.id)
            for package_detail in package_details:
                horizontal_count = 0
                if package.pallet.dimension.width % package_detail.product.dimension.width == 0 and package.pallet.dimension.depth % package_detail.product.dimension.depth == 0:
                    horizontal_count = package.pallet.dimension.width / package_detail.product.dimension.width * package.pallet.dimension.depth / package_detail.product.dimension.depth
                elif package.pallet.dimension.width % package_detail.product.dimension.depth == 0 and package.pallet.dimension.depth % package_detail.product.dimension.width == 0:
                    horizontal_count = package.pallet.dimension.width / package_detail.product.dimension.depth * package.pallet.dimension.depth / package_detail.product.dimension.width
                values = [
                    row_num - 1,  # "No"
                    package.pallet.dimension.width/10 + 4,  # Palet Genişlik
                    "X",  # X
                    package.pallet.dimension.depth/10 + 2,  # Palet Derinlik
                    f"{package_detail.product.product_type.type}.{package_detail.product.product_type.code}.{int(package_detail.product.dimension.width)}.{int(package_detail.product.dimension.depth)}.{package_detail.count}",  # KOD1
                    f"{package_detail.product.product_type.type}.{package_detail.product.product_type.code}.{int(package_detail.product.dimension.width)}.{int(package_detail.product.dimension.depth)}",  # KOD
                    0,  # Kalan
                    str(f"{package_detail.product.product_type.type}.{int(package_detail.product.dimension.depth)}"),  # Ürün Kodu
                    package_detail.product.product_type.code,  # Mod
                    "",  # Panel Boyu
                    "", # Dikey Sıra Adedi
                    "", # Kat Adedi(Dikey)
                    horizontal_count, #Yatay Sıra Adedi
                    package_detail.count / horizontal_count, # "Kat Adedi(Yatay)"
                    package_detail.count / horizontal_count, # "Eşdeğer",
                    package_detail.count,  #"Ara Toplam",
                    package_detail.count,  # Palet Adet
                    int(package_detail.count * package_detail.product.dimension.depth / 1000),  # Metre
                    round(float(package_detail.product.weight_type.std),2),  # Birim Ağırlık
                    round(float(package_detail.product.weight_type.std * package_detail.count),2),  # Net
                    round(float(package.pallet.weight),2),  # Palet Ağırlık
                    round(float(package_detail.product.weight_type.std * package_detail.count + package.pallet.weight),2)  # Toplam
                ]
                
                # Satır verilerini hücrelere yaz
                for col_num, value in enumerate(values, 1):
                    cell = ws.cell(row=row_num, column=col_num, value=value)
                    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)  # Ortalama
                    cell.border = thin_border  # Kenarlık ekle
                    
                    col_widths[col_num - 1] = max(col_widths[col_num - 1], len(str(value)))

                row_num += 1  # Sonraki satır
        
        # Toplam Satırı Ekle
        total_row = row_num
        total_label_cell = ws.cell(row=total_row, column=15, value="TOPLAM")
        total_label_cell.font = Font(bold=True)
        total_label_cell.alignment = Alignment(horizontal="center", vertical="center")
        total_label_cell.border = thin_border
        
        for col_num in range(16, 23):  # Sayısal değer içeren sütunlar (Palet Adet'ten toplam sütununa kadar)
            col_letter = get_column_letter(col_num)
            sum_formula = f"=SUM({col_letter}2:{col_letter}{total_row - 1})"
            total_cell = ws.cell(row=total_row, column=col_num, value=sum_formula)
            total_cell.font = Font(bold=True)
            total_cell.alignment = Alignment(horizontal="center", vertical="center")
            total_cell.border = thin_border  # Kenarlık ekle
            # cell.number_format = "#,##0.00"

        # Sütun genişliklerini yazılara göre ayarla
        for i, width in enumerate(col_widths):
            ws.column_dimensions[get_column_letter(i + 1)].width = width + 2  # Ekstra boşluk için "+2"

        # Dosyayı kaydet
        wb.save("uploads/report.xlsx")
