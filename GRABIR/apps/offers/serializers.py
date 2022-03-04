
from rest_framework.serializers import ModelSerializer
from GRABIR.apps.offers.models import Offer


class OfferSerializer (ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'