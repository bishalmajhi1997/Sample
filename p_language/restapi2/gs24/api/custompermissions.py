from rest_framework.permissions import BasePermission
class My_Permission(BasePermission):
    def has_permission(self, request, view):
        if request.method=="POST":
            return True
        return False