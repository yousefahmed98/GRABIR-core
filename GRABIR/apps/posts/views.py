from rest_framework import viewsets

from GRABIR.apps.posts.models import Post
from GRABIR.apps.posts.serializers import PostSerializer


# Create your views here.
class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer