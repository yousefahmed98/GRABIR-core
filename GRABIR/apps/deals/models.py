from django.db import models

from GRABIR.apps.offers.models import Offer

class Deal(models.Model):
    offer = models.ForeignKey(Offer, related_name="deal_offer",on_delete=models.CASCADE)
  