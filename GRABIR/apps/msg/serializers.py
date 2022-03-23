
from rest_framework.serializers import ModelSerializer
from GRABIR.apps.msg.models import Msg

class MsgSerializer (ModelSerializer):
    class Meta:
        model = Msg
        fields = '__all__' 