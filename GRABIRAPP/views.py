from tkinter import TRUE
from rest_framework import status
from django.shortcuts import redirect, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from .models import CustomUser, Deal, Post, Offer, Tag, PhoneNumber 
from .serializers import DealSerializer, PostSerializer, UserSerializer, OfferSerializer, TagSerializer, PhoneNumberSerializer

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


# ===============================================================Offer===============================================================

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


# ===============================================================Tags===============================================================

# ----------------------------------------------------------------
@api_view(['GET'])
def getTags(request):
    tags = Tag.objects.all()
    # many=True because function will return more than one object
    tags_serializer = TagSerializer(tags, many=True)
    return Response(tags_serializer.data)
# ----------------------------------------------------------------
@api_view(['GET'])
def getOneTag(request, tag_id):
    get_tag = Tag.objects.get(id=tag_id)
    # many=False because function will return one object
    tag_serializer = TagSerializer(get_tag, many=False)
    return Response(tag_serializer.data)
# ----------------------------------------------------------------
@api_view(['POST'])
def addTag(request):
    tag_ser = TagSerializer(data=request.data)
    if tag_ser.is_valid():
        tag_ser.save()
        return Response(tag_ser.data, status=status.HTTP_201_CREATED)
    else:
        return Response(tag_ser.errors, status=status.HTTP_400_BAD_REQUEST)
# ----------------------------------------------------------------
@api_view(['POST'])
def editTag(request, tag_id):
    tag = Tag.objects.get(id=tag_id)
    tag_ser = TagSerializer(data=request.data, instance=tag)
    if tag_ser.is_valid():
        tag_ser.save()
        return Response(tag_ser.data, status=status.HTTP_201_CREATED)
    else:
        return Response(tag_ser.errors, status=status.HTTP_400_BAD_REQUEST)
# ---------------------------------------------------------------- 
@api_view(['DELETE'])
def deleteTag(request, tag_id):
    tag = Tag.objects.get(id=tag_id)
    tag.delete()
    return Response('tag Deleted successfully!')
# ----------------------------------------------------------------

# ===============================================================PhoneNumber===============================================================

# ----------------------------------------------------------------
@api_view(['GET'])
def getPhones(request):
    phones = PhoneNumber.objects.all()
    # many=True because function will return more than one object
    phones_serializer = PhoneNumberSerializer(phones, many=True)
    return Response(phones_serializer.data)
# ----------------------------------------------------------------
@api_view(['GET'])
def getOnePhone(request, phone_id):
    get_phone = PhoneNumber.objects.get(id=phone_id)
    # many=False because function will return one object
    phone_serializer = PhoneNumberSerializer(get_phone, many=False)
    return Response(phone_serializer.data)
# ----------------------------------------------------------------
@api_view(['POST'])
def addPhone(request):
    phone_ser = PhoneNumberSerializer(data=request.data)
    if phone_ser.is_valid():
        phone_ser.save()
        return Response(phone_ser.data, status=status.HTTP_201_CREATED)
    else:
        return Response(phone_ser.errors, status=status.HTTP_400_BAD_REQUEST)
# ----------------------------------------------------------------
@api_view(['POST'])
def editPhone(request, phone_id):
    phone = PhoneNumber.objects.get(id=phone_id)
    phone_ser = PhoneNumberSerializer(data=request.data, instance=phone)
    if phone_ser.is_valid():
        phone_ser.save()
        return Response(phone_ser.data, status=status.HTTP_201_CREATED)
    else:
        return Response(phone_ser.errors, status=status.HTTP_400_BAD_REQUEST)
# ---------------------------------------------------------------- 
@api_view(['DELETE'])
def deletePhone(request, phone_id):
    phone = PhoneNumber.objects.get(id=phone_id)
    phone.delete()
    return Response('Phone Deleted successfully!')
# ---------------------------------------------------------------- 
# using viewset 
class UserViewset(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class OfferViewset(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
class TagViewset(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class DealViewset(viewsets.ModelViewSet):
    queryset = Deal.objects.all()
    serializer_class = DealSerializer

class PhoneNumberViewset(viewsets.ModelViewSet):
    queryset = PhoneNumber.objects.all()
    serializer_class = PhoneNumberSerializer

