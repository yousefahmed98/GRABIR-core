from django.db import models

# Create your models here.

class Msg(models.Model):
   body = models.CharField(max_length=200)
   email = models.CharField(max_length=100)
   subject = models.CharField(max_length=50)
   def __str__(self):
        return self.subject