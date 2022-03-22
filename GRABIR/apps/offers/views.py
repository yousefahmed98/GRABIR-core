from urllib import request
from django.shortcuts import render
from rest_framework import viewsets

from GRABIR.apps.offers.models import Offer
from GRABIR.apps.offers.serializers import OfferSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from GRABIR.apps.posts.models import Post
# Create your views here.


class OfferViewset(viewsets.ModelViewSet):
    queryset = Offer.objects.all().order_by('-id')
    serializer_class = OfferSerializer
    Authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        posts = Post.objects.all()
        postPicture = None
        print(self.request.data['post'],"/////////////////")
        for post in posts:
            print(post.id,"post.id",int(post.id) == int(self.request.data['post']))
            if int(post.id) == int(self.request.data['post']):
                print(postPicture,"*****************************")
                postPicture = post.postpicture
                print(postPicture,"*****************************")
        if self.request.user.is_authenticated:
            print(self.request.user)
            instance = serializer.save(ownerProfilePic=self.request.user.ProfilePic,
                                       offer_owner_name=self.request.user.username, postPic=postPicture)

        else:
            instance = serializer.save()

