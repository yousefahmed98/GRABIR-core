from django.contrib import admin

from GRABIR.apps.offers.models import Offer, OfferStatus

# Register your models here.
admin.site.register(Offer)
admin.site.register(OfferStatus)