from django.shortcuts import render
from rest_framework import viewsets

from GRABIR.apps.offers.models import Offer
from GRABIR.apps.offers.serializers import OfferSerializer
# Create your views here.
class OfferViewset(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer