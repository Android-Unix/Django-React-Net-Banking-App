from app_server.serializers import (
        UserSerializer, AccountSerializer, LoginSerializer
    )
from django.http import JsonResponse
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status
from django.contrib.auth.views import LoginView
from app_server.utils.utils import Utils
from app_server.models import Account
from knox.models import AuthToken


class UserHelper:
    def create_user_helper(self, data):
        serialized_user = UserSerializer(data=data)

        if serialized_user.is_valid():
            serialized_user.save()

            token = AuthToken.objects.create(user=User.objects.get(username=serialized_user.data['username']))

            with open('log.txt', 'a') as file:
                file.write('\n')
                file.write(str(token))
                file.write('\n')
                file.close()

            response_data = {
                'token': token[1],
                'user': serialized_user.data
            }
            return Response(response_data)
        else:
            return Response(serialized_user.errors)
    
    def list_user_helper(self):
        users = User.objects.all()
        serialized_user = UserSerializer(users, many=True)
        return Response(serialized_user.data)

    def user_details_helper(self, pk):
        user = User.objects.get(pk=pk)
        serialized_user = UserSerializer(user)
        return Response(serialized_user.data)

    def delete_user_helper(self, pk):
        user = User.objects.get(pk=pk)
        email = user.email
        user.delete()
        return Response(email + " deleted", status=status.HTTP_204_NO_CONTENT)


class AccountHelper:
    def create_account(self, logged_in_user, data): 
        account = {
            'logged_in_user': User.objects.get(username=logged_in_user.username),
            'account_number': Utils().account_number_generator(),
            'balance': data['balance']
        }

        serialized_account = AccountSerializer(data=account)

        with open('log.txt', 'a') as file:
            file.write(str(account))
            file.write('\n')
            file.close()

        if serialized_account.is_valid():
            serialized_account.save(logged_in_user=User.objects.get(username=logged_in_user.username), account_number=account['account_number'])
            return Response("account Created")
        else:
            return Response(serialized_account.errors)

    def list_accounts_helper(self, logged_in_user):
        accounts = Account.objects.filter(logged_in_user=User.objects.get(pk=logged_in_user.pk))

        account_list = []

        if len(accounts) > 0:
            for account in accounts:
                acc = {
                    'id': account.id,
                    'account_number': account.account_number,
                    'balance': account.balance
                }
                account_list.append(acc)
            return Response(account_list) 
        else:
            return Response("No Accounts associated to this user")

            
class LoginHelper:
    def login_helper(self, data):
        serialized_user = LoginSerializer(data=data)

        if serialized_user.is_valid():
            serialized_user.validated_data

            token = AuthToken.objects.create(user=User.objects.get(username=serialized_user.data['username']))
            response_data = {
                'token': token[1],
                'user': serialized_user.data
            }
            return Response(response_data)
        else:
            return Response(serialized_user.errors)
