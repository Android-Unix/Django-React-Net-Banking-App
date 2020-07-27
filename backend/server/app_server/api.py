from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from app_server.service.service import *
from django.contrib.auth.models import User
from rest_framework.decorators import permission_classes
from knox.auth import TokenAuthentication

from app_server.serializers import (
    UserSerializer,
    AccountSerializer,
    LoginSerializer
)

class UserAPI(viewsets.ViewSet):
    serializer_class = UserSerializer

    def create(self, request):
        return UserHelper().create_user_helper(request.data)

    def list(self, request):
        return UserHelper().list_user_helper()

    def details(self, request, pk):
        return UserHelper().user_details_helper(pk)

    def delete(self, request, pk):
        return UserHelper().delete_user_helper(pk)


@permission_classes([IsAuthenticated])
class AccountAPI(viewsets.ViewSet):
    authentication_class = (TokenAuthentication,)
    serializer_class = AccountSerializer
    
    def create_account(self, request):
        return AccountHelper().create_account(request.user, request.data)

    def list_accounts(self, request):
        return AccountHelper().list_accounts_helper(request.user)


class LoginAPI(viewsets.ViewSet):
    serializer_class = LoginSerializer

    def login(self, request):
        return LoginHelper().login_helper(request.data)
