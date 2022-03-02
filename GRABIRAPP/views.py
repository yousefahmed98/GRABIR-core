from tkinter import TRUE
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
# Create your views here.

# initialize routes function
@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/posts/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of posts'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/posts/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new post with data sent in post request'
        },
        {
            'Endpoint': '/posts/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing post with data sent in post request'
        },
        {
            'Endpoint': '/posts/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting post'
        },
    ]
    return Response(routes)

# ----------------------------------------------------------------
@api_view(['GET'])
def getPosts(request):
    posts = Post.objects.all()
    # many=True because function will return more than one object
    posts_serializer = PostSerializer(posts, many=True)
    return Response(posts_serializer.data)

# ----------------------------------------------------------------
@api_view(['GET'])
def getOnePost(request, post_id):
    post = Post.objects.get(id = post_id)
    # many=False because function will return one object
    post_serializer = PostSerializer(post, many=False)
    return Response(post_serializer.data)
