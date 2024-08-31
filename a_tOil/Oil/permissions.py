from rest_framework import permissions


class IsInTableGroup(permissions.BasePermission):
    def has_permission(self, request, view):
        groups = request.user.groups.values_list()
        if len(groups)>0:
            if request.user.is_authenticated and 'table_group' in groups:
                return True