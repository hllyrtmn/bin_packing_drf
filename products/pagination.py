from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    page_size = 1  # Varsayılan sayfa boyutu
    page_size_query_param = 'page_size'  # Kullanıcı, ?page_size= ile sayfa boyutunu belirtebilir
    max_page_size = 1  # Maksimum sayfa boyutu sınırı