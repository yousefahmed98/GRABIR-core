from base64 import urlsafe_b64encode
import datetime
from urllib import response
from xml.etree.ElementTree import QName
from django.shortcuts import redirect
from rest_framework import viewsets, generics, status
from GRABIR.apps.base.models import CustomUser
from GRABIR.apps.base.serializers import LoginSerializer, ResetPasswordSerializer, SetNewPasswordSerializer, UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from .utils import Util
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
import jwt
from django.conf import settings
from rest_framework.decorators import api_view
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str,force_bytes ,smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
# Create your views here.


class UserViewset(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class RegisterView(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        user = CustomUser.objects.get(email=user_data['email'])

        user_data["exp"] = datetime.datetime.now(
            tz=datetime.timezone.utc) + datetime.timedelta(seconds=120)
        token = jwt.encode(user_data, settings.SECRET_KEY,
                           algorithm='HS256').decode('utf-8')
        current_site = get_current_site(request).domain
        relativeLink = '/base/email-verify'
        absurl = 'http://'+current_site+relativeLink+"?token="+str(token)
        email_body = 'Hi '+user.username + \
            ' Use the link below to verify your email \n' + absurl
        data = {'email_body': email_body, 'to_email': user.email,
                'email_subject': 'Verify your email'}
        Util.send_email(data)
        return Response(user_data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def VerifyEmail(request):
    if request.method == 'GET':
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
            user = CustomUser.objects.get(id=payload['id'])
            if not user.is_verified:
                user.is_verified = True
                user.is_active = True
                user.save()
                return Response({'email': 'Successfully activated'}, status=status.HTTP_200_OK)
            else:
                return Response({'email': 'already activated'}, status=status.HTTP_204_NO_CONTENT)
        except jwt.ExpiredSignatureError as identifier:
            return Response({'error': 'Activation Token Expired'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)



class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class RequestResetPassword(generics.GenericAPIView):
    serializer_class = ResetPasswordSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        email = request.data.get('email', '')
        if CustomUser.objects.filter(email=email).exists():
            user = CustomUser.objects.get(email=email)
            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            token = PasswordResetTokenGenerator().make_token(user)
            current_site = get_current_site(
                request=request).domain
            relativeLink = reverse(
                'password-reset-confirm', kwargs={'uidb64': uidb64, 'token': token})

            redirect_url = request.data.get('redirect_url', '')
            absurl = 'http://'+current_site + relativeLink
            email_body = 'Hello, \n Use link below to reset your password  \n' + \
                absurl+"?redirect_url="+redirect_url
            data = {'email_body': email_body, 'to_email': user.email,
                    'email_subject': 'Reset your passsword'}
            Util.send_email(data)
        return Response({'success': 'We have sent you a link to reset your password'}, status=status.HTTP_200_OK)


class RestPasswordTokenCheckAPI(generics.GenericAPIView):
    serializer_class = SetNewPasswordSerializer

    def get(self, request, uidb64, token):
        
        redirect_url = request.GET.get('redirect_url')
        try:
            id = smart_str(urlsafe_base64_decode(uidb64))
            user = CustomUser.objects.get(id=id)
            if not PasswordResetTokenGenerator().check_token(user, token):
                response = redirect(redirect_url+'?token_valid=False')
                return response
            if redirect_url and len(redirect_url) > 3:
                response = redirect(redirect_url+'?token_valid=True&uidb64='+uidb64+'&token='+token)
                return response
        except DjangoUnicodeDecodeError as identifier:
            try:
                if not PasswordResetTokenGenerator().check_token(user):
                    return Response(redirect_url+'?token_valid=False')
                    
            except UnboundLocalError as e:
                return Response({'error': 'Token is not valid, please request a new one'}, status=status.HTTP_400_BAD_REQUEST)

class SetNewPasswordAPIView(generics.GenericAPIView):
    serializer_class = SetNewPasswordSerializer

    def patch(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'success': True, 'message': 'Password reset success'}, status=status.HTTP_200_OK)