from tkinter import TRUE
from rest_framework import status
from django.shortcuts import redirect, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CustomUser, Post
from .serializers import PostSerializer, UserSerializer
# Create your views here.

# # initialize routes function
# @api_view(['GET'])
# def getRoutes(request):
#     return Response(routes)

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

# ===============================================================User===============================================================

# ----------------------------------------------------------------
@api_view(['GET'])
def getUsers(request):
    users = CustomUser.objects.all()
    # many=True because function will return more than one object
    users_serializer = UserSerializer(users, many=True)
    return Response(users_serializer.data)

# ----------------------------------------------------------------
@api_view(['GET'])
def getOneUser(request, user_id):
    get_user = CustomUser.objects.get(id=user_id)
    # many=False because function will return one object
    user_serializer = UserSerializer(get_user, many=False)
    return Response(user_serializer.data)

# ----------------------------------------------------------------
@api_view(['POST'])
def addUser(request):
    user_ser = UserSerializer(data=request.data)
    if user_ser.is_valid():
        user_ser.save()
        return Response(user_ser.data, status=status.HTTP_201_CREATED)
    else:
        return Response(user_ser.errors, status=status.HTTP_400_BAD_REQUEST)
    
# ---------------------------------------------------------------- 
@api_view(['POST'])
def editUser(request, user_id):
    student = CustomUser.objects.get(id=user_id)
    user_ser = UserSerializer(data=request.data, instance=student)
    if user_ser.is_valid():
        user_ser.save()
        return Response(user_ser.data, status=status.HTTP_201_CREATED)
    else:
        return Response(user_ser.errors, status=status.HTTP_400_BAD_REQUEST)

# ---------------------------------------------------------------- 
@api_view(['DELETE'])
def deleteUser(request, user_id):
    user = CustomUser.objects.get(id=user_id)
    user.delete()
    return Response('User Deleted successfully!')


    