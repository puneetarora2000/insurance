from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from polling.serializers import UserSerializer
from .permissions import *


# class UserView(viewsets.ModelViewSet):
#     serializer_class = UserSerializer
#     model = User
#
#     def get_permissions(self):
#         # allow non-authenticated user to create via POST
#         return (AllowAny() if self.request.method == 'POST'
#                 else IsStaffOrTargetUser()),
#
#
# class IsStaffOrTargetUser():
#     def has_permission(self, request, view):
#         # allow user to list all users if logged in user is staff
#         return view.action == 'retrieve' or request.user.is_staff
#
#     def has_object_permission(self, request, view, obj):
#         # allow logged in user to view own details, allows staff to view all records
#         return request.user.is_staff or obj == request.user