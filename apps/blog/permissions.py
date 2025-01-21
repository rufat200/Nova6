from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.method in ['GET', 'HEAD', 'OPTIONS'] or obj.user == request.user