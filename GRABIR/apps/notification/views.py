from django.shortcuts import render
from rest_framework import viewsets ,generics
from GRABIR.apps.notification.models   import Notification
from GRABIR.apps.notification.serializers import NotificationSerializer
from rest_framework.authentication import TokenAuthentication 
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class NotificationViewset(viewsets.ModelViewSet):
    queryset = Notification.objects.all().order_by('-id')
    serializer_class = NotificationSerializer    
    Authentication_classes  = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            instance = serializer.save(from_user_ProfilePic=self.request.user.ProfilePic ,from_user_name= self.request.user.username)
        else:
            instance = serializer.save()


