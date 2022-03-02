from rest_framework.serializers import ModelSerializer
from .models import Post, CustomUser
class PostSerializer (ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class UserSerializer (ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        