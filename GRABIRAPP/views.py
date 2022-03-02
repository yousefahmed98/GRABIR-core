from tkinter import TRUE
from rest_framework import status
from django.shortcuts import redirect, render
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

# ===============================================================POST===============================================================

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
    get_post = Post.objects.get(id=post_id)
    # many=False because function will return one object
    post_serializer = PostSerializer(get_post, many=False)
    return Response(post_serializer.data)

# ----------------------------------------------------------------
@api_view(['POST'])
def addPost(request):
    post_ser = PostSerializer(data=request.data)
    if post_ser.is_valid():
        post_ser.save()
        return Response(post_ser.data, status=status.HTTP_201_CREATED)
    else:
        return Response(post_ser.errors, status=status.HTTP_400_BAD_REQUEST)
    
# ---------------------------------------------------------------- 
@api_view(['POST'])
def editPost(request, post_id):
    student = Post.objects.get(id=post_id)
    post_ser = PostSerializer(data=request.data, instance=student)
    if post_ser.is_valid():
        post_ser.save()
        return Response(post_ser.data, status=status.HTTP_201_CREATED)
    else:
        return Response(post_ser.errors, status=status.HTTP_400_BAD_REQUEST)

# ---------------------------------------------------------------- 
@api_view(['DELETE'])
def deletePost(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return Response('Post Deleted successfully!')

    