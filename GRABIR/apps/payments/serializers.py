
from rest_framework.serializers import ModelSerializer
from GRABIR.apps.payments.models import Payment


class PaymentSerializer (ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'