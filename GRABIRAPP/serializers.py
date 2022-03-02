from rest_framework.serializers import ModelSerializer
from .models import Post, Offer
class PostSerializer (ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
    
class OfferSerializer (ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'
        