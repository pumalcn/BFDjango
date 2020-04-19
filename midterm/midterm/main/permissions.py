from rest_framework.permissions import IsAuthenticated, BasePermission
from midterm.auth_.models import MainUser


class JournalPermission(BasePermission):
    message = 'You must be the authenticated.'

    def has_permission(self, request, view):
        if view.action is 'create':
            return request.user.is_superuser or request.user.is_store_admin
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False
        if view.action is not 'retrieve':
            return request.user.is_superuser or request.user.is_store_admin
        return True


class BookPermission(BasePermission):
    message = 'You must be authenticated.'

    def has_permission(self, request, view):
        if view.action is 'create':
            return request.user.is_superuser or request.user.is_store_admin
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False
        if view.action is not 'retrieve':
            return request.user.is_superuser or request.user.is_store_admin
        return True
