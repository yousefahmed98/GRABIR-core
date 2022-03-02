from tkinter import TRUE
from rest_framework import status
from django.shortcuts import redirect, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post,Offer
from .serializers import PostSerializer, OfferSerializer
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
# ---------------------------------------------------------------- 
# ---------------------------------------------------------------- 

@api_view(['GET'])
def getOffers(request):
    offers = Offer.objects.all()
    # many=True because function will return more than one object
    offers_serializer = OfferSerializer(offers, many=True)
    return Response(offers_serializer.data)

# ----------------------------------------------------------------
@api_view(['GET'])
def getOneOffer(request, offer_id):
    get_offer = Offer.objects.get(id=offer_id)
    # many=False because function will return one object
    offer_serializer = OfferSerializer(get_offer, many=False)
    return Response(offer_serializer.data)
# ----------------------------------------------------------------
@api_view(['POST'])
def addOffer(request):
    offer_ser = OfferSerializer(data=request.data)
    if offer_ser.is_valid():
        offer_ser.save()
        return Response(offer_ser.data, status=status.HTTP_201_CREATED)
    else:
        return Response(offer_ser.errors, status=status.HTTP_400_BAD_REQUEST)
# ---------------------------------------------------------------- 
@api_view(['POST'])
def editOffer(request, offer_id):
    offer = Offer.objects.get(id=offer_id)
    offer_ser = OfferSerializer(data=request.data, instance=offer)
    if offer_ser.is_valid():
        offer_ser.save()
        return Response(offer_ser.data, status=status.HTTP_201_CREATED)
    else:
        return Response(offer_ser.errors, status=status.HTTP_400_BAD_REQUEST)
# ---------------------------------------------------------------- 
@api_view(['DELETE'])
def deleteOffer(request, offer_id):
    offer = Offer.objects.get(id=offer_id)
    offer.delete()
    return Response('Offer Deleted successfully!')
# ---------------------------------------------------------------- 