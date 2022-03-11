from rest_framework.serializers import ModelSerializer
from GRABIR.apps.base.models import PhoneNumber, CustomUser
from rest_framework import serializers
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed


class UserSerializer (ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }


class PhoneNumberSerializer (ModelSerializer):
    class Meta:
        model = PhoneNumber
        fields = '__all__'


class RegisterSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password']


class LoginSerializer(ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)
    username = serializers.CharField(
        max_length=255, min_length=3, read_only=True)

    tokens = serializers.SerializerMethodField()
    def get_tokens(self, obj):
        user = CustomUser.objects.get(email=obj['email'])

        return {
            'refresh': user.tokens()['refresh'],
            'access': user.tokens()['access']
        }
    class Meta:
        model=CustomUser 
        fields = ['email','password','username','tokens']

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        user = auth.authenticate(username=email, password=password)
        if not user:
            raise AuthenticationFailed("'invalid email or password") 
        if not user.is_verified:
            raise AuthenticationFailed("Email not verified")
        return {
            'email': user.email,
            'username': user.username,
            'tokens': user.tokens
        }
