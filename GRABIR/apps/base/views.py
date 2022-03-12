import datetime
from xml.etree.ElementTree import QName
from rest_framework import viewsets, generics, status
from GRABIR.apps.base.models import CustomUser
from GRABIR.apps.base.serializers import LoginSerializer, UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from .utils import Util
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
import jwt
from django.conf import settings
from rest_framework.decorators import api_view
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
        absurl = 'http://'+str(current_site)+str(relativeLink)+'?token='+str(token)
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