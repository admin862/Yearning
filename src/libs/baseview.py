from rest_framework.permissions import (
    IsAdminUser,
    IsAuthenticated,
    BasePermission
)
from core.models import globalpermissions
from rest_framework.views import APIView


class BaseView(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request, args: str = None):
        pass

    def post(self, request, args: str = None):
        pass

    def put(self, request, args: str = None):
        pass

    def delete(self, request, args: str = None):
        pass


class SuperUserpermissions(APIView):
    
    permission_classes = (IsAdminUser,)

    def get(self, request, args: str = None):
        pass

    def post(self, request, args: str = None):
        pass

    def put(self, request, args: str = None):
        pass

    def delete(self, request, args: str = None):
        pass


class AnyLogin(APIView):

    permission_classes = ()
    authentication_classes = ()

    def get(self, request, args: str = None):
        pass

    def post(self, request, args: str = None):
        pass

    def put(self, request, args: str = None):
        pass

    def delete(self, request, args: str = None):
        pass


'''

平台页面权限permission

'''


class WebPermission(BasePermission):

    def has_permission(self, request, view):
        permission = globalpermissions.objects.filter(authorization=request.user).first()
        if permission is not None and permission.dingding == 0:
            return True
