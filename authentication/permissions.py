from rest_framework import permissions


def is_method_read_only(request):
    return request.method in permissions.SAFE_METHODS


class IsAdminUserOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return is_method_read_only(request) or (request.user and request.user.is_staff)


class ShoppingCartAccessPermission(permissions.IsAuthenticated):
    message = 'Action not allowed.'

    def has_permission(self, request, view):
        try:
            is_client = request.user.group.filter(name='client').exist()
        except AttributeError:
            return False
        else:
            return is_client or (request.user and request.user.is_staff)

    def has_object_permission(self, request, view, obj):
        return request.method != "DELETE" or (request.user and request.user.is_staff)


class OrderAccessPermission(permissions.IsAuthenticated):
    message = 'Action haha not allowed.'

    def has_permission(self, request, view):
        try:
            is_merchant = request.user.group.filter(name='merchant').exist()
        except AttributeError:
            return False
        else:
            if is_merchant and request.method == 'DELETE':
                return False
            else:
                return True

    def has_object_permission(self, request, view, obj):
        return request.method != "DELETE" or (request.user and request.user.is_staff)


class ProductAccessPermission(permissions.IsAuthenticatedOrReadOnly):
    message = 'Action not allowed.'

    def has_permission(self, request, view):

        if is_method_read_only(request):
            return True

        if (request.user and request.user.is_staff) or request.user.group.filter(name='merchant').exist():
            return True

        return False

    def has_object_permission(self, request, view, obj):
        if is_method_read_only(request) or request.user.is_staff or request.user.group.filter(name='merchant').exist():
            return True

        return False