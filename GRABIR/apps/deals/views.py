from django.shortcuts import render
from rest_framework import viewsets
from GRABIR.apps.deals.models import Deal
from GRABIR.apps.deals.serializers import DealSerializer

# Create your views here.
class DealViewset(viewsets.ModelViewSet):
    queryset = Deal.objects.all()
    serializer_class = DealSerializer