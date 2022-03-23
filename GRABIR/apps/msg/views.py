from django.shortcuts import render
from rest_framework import viewsets
from GRABIR.apps.msg.models import Msg
from GRABIR.apps.msg.serializers import MsgSerializer

# Create your views here.
class MsgViewset(viewsets.ModelViewSet):
    queryset = Msg.objects.all()
    serializer_class = MsgSerializer