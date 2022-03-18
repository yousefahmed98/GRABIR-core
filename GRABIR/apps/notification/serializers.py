
from rest_framework.serializers import ModelSerializer
from GRABIR.apps.notification.models   import Notification

class NotificationSerializer (ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'


