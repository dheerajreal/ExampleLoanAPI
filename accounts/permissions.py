from rest_framework import permissions


class AdminPermission(permissions.BasePermission):
    message = "User is not an admin"

    def has_permission(self, request, view):
        return request.user.is_admin or request.user.is_staff


class AgentPermission(permissions.BasePermission):
    message = "User is not an agent"

    def has_permission(self, request, view):
        return request.user.is_admin or request.user.is_agent
