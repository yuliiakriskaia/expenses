from rest_framework import permissions
from serializers import Group


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class CanManageRecords(permissions.BasePermission):
    def has_permission(self, request, view):
        admin = Group.objects.get(name='admin')
        user = Group.objects.get(name='regular_user')
        if admin in request.user.groups.all() or user in request.user.groups.all():
            return True
        return False


class CanManageUsers(permissions.BasePermission):
    def has_permission(self, request, view):
        user_manager = Group.objects.get(name='user_manager')
        admin = Group.objects.get(name='admin')
        if user_manager in request.user.groups.all() or admin in request.user.groups.all():
            return True
        return False




