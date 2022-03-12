from rest_framework import viewsets ,generics

from GRABIR.apps.posts.models import Post , Tag
from GRABIR.apps.posts.serializers import PostSerializer , TagSerializer
from rest_framework.authentication import TokenAuthentication 
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer  
    Authentication_classes  = [TokenAuthentication]

class TagsViewset(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer  
    # Authentication_classes  = [TokenAuthentication]