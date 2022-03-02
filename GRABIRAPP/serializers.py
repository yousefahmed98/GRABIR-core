from rest_framework.serializers import ModelSerializer

from .models import Deal, Post, CustomUser, Offer ,Tag, PhoneNumber

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

class TagSerializer (ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class PhoneNumberSerializer (ModelSerializer):
    class Meta:
        model = PhoneNumber
        fields = '__all__'

       
class DealSerializer (ModelSerializer):
    class Meta:
        model = Deal
        fields = '__all__' 
        