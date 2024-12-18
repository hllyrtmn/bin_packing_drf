import copy
from typing import List

from logistics.models import PackageDetail,Package, Pallet
from orders.models import OrderDetail


class CalculatePackageService:
    @staticmethod
    def save_packages_and_details_to_db(package_details,order_id):
        """
        Gelen package_details verilerini kullanarak Package ve PackageDetail kayıtlarını oluşturur.
        """
        package_map = {}

        for detail_data in package_details:
            # Package oluştur veya al
            
            package_id = detail_data.package_id
            if package_id not in package_map:
                package = Package.objects.create(
                    id=package_id,
                    order_id=order_id,
                    pallet_id=detail_data.package.pallet_id
                )
                package_map[package_id] = package
            else:
                package = package_map[package_id]


            PackageDetail.objects.create(
                package_id = package.id,
                product_id = detail_data.product_id,
                count = detail_data.count
            )
        return 1
            
        
    
    @staticmethod
    def create_packages(order_details:List[OrderDetail],pallets:List[Pallet]):
        package_details:List[PackageDetail]
        packages:List[Package]
        
        remaining_products,package_details,packages =  CalculatePackageService.place_products_in_pallets(order_details, pallets)
        
        if remaining_products:
            remaining_packages,packages_remaining = CalculatePackageService.place_remaining_products_in_boxes(remaining_products, pallets)
            package_details.extend(remaining_packages)
            packages.extend(packages_remaining)
            
        return package_details
        
     
    @staticmethod
    def place_remaining_products_in_boxes(remaining_order_details:List[OrderDetail],pallets:List[Pallet]):
        package_details:List[PackageDetail] = []
        packages:List[Package] = []
        grouped_order_details = CalculatePackageService.group_products_by_dimension(remaining_order_details)
        for group in grouped_order_details:
            while group:
                best_pallet = CalculatePackageService.find_best_box_for_group(group,pallets)
                if not best_pallet:
                    break
                total_quantity = sum(order_detail.count for order_detail in group)
                items_per_layer = (best_pallet.dimension.width // max(order_detail.product.dimension.width for order_detail in group)) * (best_pallet.dimension.depth // max(order_detail.product.dimension.depth for order_detail in group))
                layers_per_box = best_pallet.dimension.height // group[0].product.dimension.height
                total_capacity = items_per_layer * layers_per_box
                
                boxes_needed = int((total_quantity + total_capacity - 1) // total_capacity)
                
                for _ in range(boxes_needed):
                    if total_quantity <= 0:
                        break
                    placed_quantity = min(total_capacity, total_quantity)
                    total_placed = 0
                    
                    package=Package(order=None,pallet=best_pallet)
                    packages.append(package)
                    for order_detail in group:
                        if total_placed >= placed_quantity:
                            package.order = order_detail.order
                            break
                        package_detail_instance = PackageDetail(package = package,product=order_detail.product,count=0)
                        while order_detail.count > 0 and total_placed < placed_quantity:
                            order_detail.count -= 1
                            total_placed += 1
                            package_detail_instance.count += 1
                        if package_detail_instance.count > 0:
                            package_details.append(package_detail_instance)
                    group = [order_detail for order_detail in group if order_detail.count > 0]       
                    total_quantity -= placed_quantity 
                    if total_quantity == 0:
                        break
                    if best_pallet != CalculatePackageService.find_best_box_for_group(group,pallets):
                        break
                            
        return package_details,packages
    
    @staticmethod
    def find_best_box_for_group(group, pallets):
        max_depth = max(order_detail.product.dimension.depth for order_detail in group)
        max_width = max(order_detail.product.dimension.width for order_detail in group)
        
        best_pallet = None
        for pallet in pallets:
            
            if (pallet.dimension.width % max_width == 0 and pallet.dimension.depth % max_depth == 0) or (pallet.dimension.width % max_depth == 0 and pallet.dimension.depth % max_width == 0):
                
                if(pallet.dimension.width % max_depth == 0 and pallet.dimension.depth % max_width == 0):
                    pallet.dimension.width, pallet.dimension.depth = pallet.dimension.depth, pallet.dimension.width
                best_pallet = pallet
                
                return best_pallet
    
    @staticmethod
    def group_products_by_dimension(remaining_order_details:List[OrderDetail]):
        grouped_by_width = {}
        for remaining_order_detail in remaining_order_details:
            width_key = int(remaining_order_detail.product.dimension.width)
            if width_key not in grouped_by_width:
                grouped_by_width[width_key] = []
            grouped_by_width[width_key].append(remaining_order_detail)
        
        for width_key, order_details in grouped_by_width.items():
            grouped_by_width[width_key] = sorted(order_details, key=lambda order_detail: order_detail.product.dimension.depth, reverse=True)

        return list(grouped_by_width.values())
            
    @staticmethod
    def place_products_in_pallets(order_details:List[OrderDetail],pallets:List[Pallet]):
        
        remaining_products = []
        package_details:List[PackageDetail] = []
        packages:List[Package] = []
        
        for order_detail in order_details:
            remaining_quantity = order_detail.count
            for pallet in pallets:
                if CalculatePackageService.can_fit_exactly(order_detail, pallet):
                    items_per_layer = int(CalculatePackageService.calculate_items_per_layer_exactly(order_detail, pallet))
                    layers_per_box = int(pallet.dimension.height // order_detail.product.dimension.height)
                    total_capacity = int(items_per_layer * layers_per_box)
                    
                    remove_product_quantity  =  int(order_detail.count - total_capacity)
                    if(remove_product_quantity > 0):
                        remove_product_quantity = (remove_product_quantity % total_capacity)
                        if(remove_product_quantity > 0):
                            copy_order_detail = copy.deepcopy(order_detail)
                            copy_order_detail.count = remove_product_quantity
                            order_detail.count -= remove_product_quantity
                            remaining_products.append(copy_order_detail)
                    elif(remove_product_quantity < 0):
                        remaining_products.append(order_detail)
                        break
                    if total_capacity > 0:
                        boxes_needed = (order_detail.count + total_capacity - 1) // total_capacity  # Round up
                        
                        
                        placed_quantity_per_box = min(remaining_quantity, int(total_capacity))
                        
                        for _ in range(int(boxes_needed)):
                            if remaining_quantity <= 0:
                                break
                            package=Package(order=order_detail.order,pallet=pallet)
                            packages.append(package)
                            placed_quantity = min(placed_quantity_per_box, remaining_quantity)
                            
                            package_detail_instance = PackageDetail(package = package,product=order_detail.product,count=placed_quantity) 
                            
                            package_details.append(package_detail_instance)
                            
                            remaining_quantity -= placed_quantity
                            
                        remaining_quantity -= total_capacity * boxes_needed
                        if remaining_quantity <= 0 or total_capacity > remaining_quantity:
                            break
        return remaining_products,package_details,packages
    
    @staticmethod
    def can_fit_exactly(order_detail:OrderDetail, pallet:Pallet):
        return (pallet.dimension.width % order_detail.product.dimension.width == 0 and pallet.dimension.depth % order_detail.product.dimension.depth == 0) or \
           (pallet.dimension.width % order_detail.product.dimension.depth == 0 and pallet.dimension.depth % order_detail.product.dimension.width == 0)
    
    @staticmethod
    def calculate_items_per_layer_exactly(order_detail:OrderDetail, pallet:Pallet):
        if pallet.dimension.width % order_detail.product.dimension.width == 0 and pallet.dimension.depth % order_detail.product.dimension.depth == 0:
            items_per_layer = (pallet.dimension.width // order_detail.product.dimension.width) * (pallet.dimension.depth // order_detail.product.dimension.depth)
        else:
            items_per_layer = (pallet.dimension.width // order_detail.product.dimension.depth) * (pallet.dimension.depth // order_detail.product.dimension.width)
        return items_per_layer