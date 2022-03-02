from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator
# Create your models here.
class CustomUser(AbstractUser):
    region = models.CharField(max_length=200)
    passport_img = models.FileField(upload_to='images/', null=True, verbose_name="passport image")
class Tag(models.Model):
    class Meta:
        ordering = ['pk']
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Post(models.Model):
    class Meta:
        ordering = ['pk']
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    postpicture = models.FileField(upload_to='images/', null=True, verbose_name="Post Picture")
    created_at = models.DateField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    from_region= models.CharField(null=True,max_length=50)
    to   = models.CharField(null=True,max_length=50)
    tags = models.ManyToManyField(Tag, through='PostTags')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    price = models.FloatField(null=True)

    
    def show_tags(self):
        return "\n".join([a.name for a in self.tags.all()])

    def __str__(self):
        return self.title + ' | ' + str(self.user)

class PostTags(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

class PhoneNumber(models.Model):
    # phone =models.CharField(max_length=11) 
    # phone = PhoneNumberField(unique = True, null = True, blank = False) 
    phoneNumberRegex = RegexValidator(regex = r"^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\./0-9]*$")
    phoneNumber = models.CharField(validators = [phoneNumberRegex], max_length = 16, unique = True,null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#^01[0-2]\d{1,8}$
#^(\+\d{1,3})?,?\s?\d{8,13}
class OfferStatus(models.Model):
    status = models.CharField(max_length=50)  

class Offer(models.Model):
    details = models.CharField(max_length=300)
    from_region= models.CharField(null=True,max_length=50)
    to_region   = models.CharField(null=True,max_length=50) 
    price = models.FloatField()
    delivery_date = models.DateField(auto_now_add=True,null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    status = models.ForeignKey(OfferStatus, on_delete=models.CASCADE)

class Deal(models.Model):
    offer_id = models.ForeignKey(OfferStatus, on_delete=models.CASCADE)


