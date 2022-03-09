from django.shortcuts import render
from rest_framework import viewsets

from GRABIR.apps.payments.models import Payment
from GRABIR.apps.payments.serializers import PaymentSerializer
# Create your views here.
class PaymentViewset(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer