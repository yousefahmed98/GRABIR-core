from datetime import datetime
from django.db import models
from GRABIR.apps.base.models import CustomUser

from GRABIR.apps.posts.models import Post


class OfferStatus(models.Model):
    LOCATOR_YES_NO_CHOICES = ((None, ''), (True, 'Yes'), (False, 'No'))
    # status = models.BooleanField(nul)
    status = models.BooleanField(choices=LOCATOR_YES_NO_CHOICES,
                      max_length=3,
                      blank=True, null=True, default=None,)


class Offer(models.Model):
    details = models.CharField(max_length=300)
    from_region = models.CharField(null=True, max_length=50)
    to_region = models.CharField(null=True, max_length=50)
    price = models.FloatField()
    delivery_date = models.DateField(auto_now_add=True, null=True)
    created_at = models.DateTimeField(default=datetime.now(), blank=False)
    post = models.ForeignKey(
        Post, related_name="offer_post", on_delete=models.CASCADE)
    status = models.ForeignKey(
        OfferStatus, related_name="offer_status", on_delete=models.CASCADE, null=True)
    offer_owner = models.ForeignKey(
        CustomUser, related_name="offer_user", on_delete=models.CASCADE)

    def __str__(self):
        return self.details
