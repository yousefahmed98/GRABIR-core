from django.db import models
from GRABIR.apps.base.models import CustomUser

from GRABIR.apps.posts.models import Post

class OfferStatus(models.Model):
    status = models.CharField(max_length=50)  

class Offer(models.Model):
    details = models.CharField(max_length=300)
    from_region= models.CharField(null=True,max_length=50)
    to_region   = models.CharField(null=True,max_length=50) 
    price = models.FloatField()
    delivery_date = models.DateField(auto_now_add=True,null=True)
    post = models.ForeignKey(Post,related_name="offer_post", on_delete=models.CASCADE)
    status = models.ForeignKey(OfferStatus,related_name="offer_status", on_delete=models.CASCADE)
    offer_owner = models.ForeignKey(CustomUser, related_name="offer_user",on_delete=models.CASCADE)
