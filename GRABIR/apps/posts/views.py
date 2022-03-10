from rest_framework import viewsets ,generics

from GRABIR.apps.posts.models import Post
from GRABIR.apps.posts.serializers import PostSerializer
from rest_framework.authentication import TokenAuthentication 
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer    
    Authentication_classes  = [TokenAuthentication]
    