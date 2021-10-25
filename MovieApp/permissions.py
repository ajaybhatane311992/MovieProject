from rest_framework.permissions import BasePermission,SAFE_METHODS

# Built In permissions

class IsReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:  # Only GET method
            return True
        else:
            return False

# Custome Permissions for GET,POST,PUT
class IsGetOrPostOrPut(BasePermission):
    def has_permission(self, request, view):
        allowed_methods=['GET','POST','PUT']  # Create custom methods
        if request.method in allowed_methods:
            return True
        else:
            return False

# Custome Permissions for GET,POST
class IsGetOrPost(BasePermission):
    def has_permission(self, request, view):
        allowed_methods=['GET','POST']
        if request.method in allowed_methods:
            return True
        else:
            return False
