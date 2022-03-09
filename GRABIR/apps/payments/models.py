from django.db import models
from GRABIR.apps.base.models import CustomUser

class PaymentStatus(models.Model):
    status = models.CharField(max_length=50)  

class Payment(models.Model):
    from_user =  models.ForeignKey(CustomUser, related_name="payment_from_user",on_delete=models.CASCADE)
    to_usr = models.ForeignKey(CustomUser, related_name="payment_to_user",on_delete=models.CASCADE)
    total = models.FloatField()
    status = models.ForeignKey(PaymentStatus,related_name="payment_status", on_delete=models.CASCADE)
