from django.db import models
from GRABIR.apps.base.models import CustomUser

# Create your models here.

class Rate(models.Model):
    stars = models.IntegerField(max_length=5)
    review = models.CharField(max_length=30)
    user = models.ForeignKey(CustomUser, related_name="rate_user", on_delete=models.CASCADE)

    def __str__(self):
        return self.stars