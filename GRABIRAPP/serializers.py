from rest_framework.serializers import ModelSerializer

from .models import Post, CustomUser, Offer ,Tag, PhoneNumber

class PostSerializer (ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class UserSerializer (ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
   
class OfferSerializer (ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'

class TagsSerializer (ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class PhoneNumberSerializer (ModelSerializer):
    class Meta:
        model = PhoneNumber
        fields = '__all__'

        
        