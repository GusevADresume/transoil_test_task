from rest_framework import permissions


class IsInTableGroup(permissions.BasePermission):
    def has_permission(self, request, view):
        groups = request.user.groups.values_list()
        if len(groups) > 0:
            groups_list = [i[1] for i in groups]
            if request.user.is_authenticated and 'table_group' in groups_list:
                return True
