from rest_framework import viewsets
from GRABIR.apps.base.models import CustomUser
from GRABIR.apps.base.serializers import UserSerializer

# Create your views here.

class UserViewset(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer