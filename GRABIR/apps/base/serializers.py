from rest_framework.serializers import ModelSerializer
from GRABIR.apps.base.models import PhoneNumber, CustomUser


class UserSerializer (ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class PhoneNumberSerializer (ModelSerializer):
    class Meta:
        model = PhoneNumber
        fields = '__all__'
