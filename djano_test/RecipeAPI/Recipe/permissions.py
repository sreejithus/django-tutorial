from rest_framework.permissions import BasePermission



# class AdminorReadonly(BasePermission):
#              def has_permission(self, request, view):
#                       if request.method=='GET':
#                                 return request.user.is_autheticated
#                       return request.user.is_authenticated and request.user.is_superuser


class Isowner(BasePermission):
         message="only owner can update "
         def has_object_permission(self, request, view, obj):
                 return  obj.user==request.user