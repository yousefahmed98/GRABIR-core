
from rest_framework.serializers import ModelSerializer
from GRABIR.apps.deals.models import Deal

class DealSerializer (ModelSerializer):
    class Meta:
        model = Deal
        fields = '__all__' 