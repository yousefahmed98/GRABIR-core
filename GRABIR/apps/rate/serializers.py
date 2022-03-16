
from rest_framework.serializers import ModelSerializer
from GRABIR.apps.rate.models import Rate


class RateSerializer (ModelSerializer):
    class Meta:
        model = Rate
        fields = '__all__'