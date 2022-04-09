from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminUserOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        
        if request.method in SAFE_METHODS:
            return True

        return request.user.is_superuser


class AdminUserCantPOST(BasePermission):
    
    def has_permission(self, request, view):
        if request.method=='POST' and request.user.is_superuser:
            return False
        
        return True
