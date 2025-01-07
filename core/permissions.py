from rest_framework.permissions import BasePermission
from orders.models import CompanyUser

class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        return request.user and request.user.is_authenticated
class IsCompanyMember(BasePermission):
    
    
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
    def has_object_permission(self, request, view, obj):
         return CompanyUser.objects.filter(user=request.user, company=obj.company).exists()