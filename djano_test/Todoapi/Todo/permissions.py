from rest_framework.permissions import BasePermission


class Isowner(BasePermission):
           message="only owner can update "
           def has_object_permission(self, request, view, obj):
                   return obj.user == request.user