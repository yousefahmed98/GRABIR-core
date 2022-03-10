from rest_framework.serializers import ModelSerializer
from GRABIR.apps.base.models import PhoneNumber, CustomUser


class UserSerializer (ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        extra_kwargs = {
            'password' : {'write_only':True}
        }

class PhoneNumberSerializer (ModelSerializer):
    class Meta:
        model = PhoneNumber
        fields = '__all__'


class RegisterSerializer(ModelSerializer):
     class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password']