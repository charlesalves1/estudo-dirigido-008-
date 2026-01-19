from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name="Administrador").exists()


class IsProfessor(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name="Professor(a)").exists()


class IsTecnico(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name="Técnico").exists()


class IsUsuario(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name="Usuário(a)").exists()
