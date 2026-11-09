from rest_framework.permissions import BasePermission



class Iscustomer(BasePermission):
              def has_permission(self, request, view):
                               if request.method == 'GET':
                                            return request.user.is_authenticated
                               return request.user.is_authenticated and request.user.role =="customer"
              def has_object_permission(self, request, view, obj):
                               return request.user == obj.user 