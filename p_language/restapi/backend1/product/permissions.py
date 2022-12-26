from rest_framework import permissions
class IsStaffEditorPermission(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        user=request.user
        print(user.get_all_permissions())
        if user.is_staff:
            if user.has_perm("products.add_product"):#app_name.verb_modelname
                return True
            if user.has_perm("products.delete_product"):
                return True
                