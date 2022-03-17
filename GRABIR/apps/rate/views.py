from django.shortcuts import render
from GRABIR.apps.rate.models import Rate
from GRABIR.apps.rate.serializers import RateSerializer
from rest_framework import viewsets
# Create your views here.

class RateViewset(viewsets.ModelViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer