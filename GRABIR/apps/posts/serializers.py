
from rest_framework.serializers import ModelSerializer
from GRABIR.apps.posts.models import Post,Tag

class PostSerializer (ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class TagSerializer (ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
