from rest_framework import viewsets,generics,status
from GRABIR.apps.base.models import CustomUser
from GRABIR.apps.base.serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from .utils import Util
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
import jwt
from django.conf import settings
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

        token = RefreshToken.for_user(user).access_token
        current_site = get_current_site(request).domain
        print(current_site)
        relativeLink = reverse('email-verify')
        print(relativeLink)
        absurl = 'http://'+current_site+relativeLink+"?token="+str(token)
        email_body = 'Hi '+user.username + \
            ' Use the link below to verify your email \n' + absurl
        data = {'email_body': email_body, 'to_email': user.email,
                'email_subject': 'Verify your email'}      
        Util.send_email(data)
        return Response(user_data,status=status.HTTP_201_CREATED)


class VerifyEmail(generics.GenericAPIView):
    def get(self,request):
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        token = request.GET.get('token')
        
        print(token)
        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
            print(payload)
            user = CustomUser.objects.get(id=payload['user_id'])
        except jwt.ExpiredSignatureError as identifier:
            return Response({'error': 'Activation Expired'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)
        


    