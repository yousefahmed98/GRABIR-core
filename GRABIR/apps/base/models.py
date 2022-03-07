from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

# Create your models here.
class CustomUser(AbstractUser):
    region = models.CharField(max_length=200)
    passport_img = models.FileField(upload_to='images/', null=True, verbose_name="passport image")
    email = models.EmailField(_('email address'),blank=False,unique=True,db_index=True)
    is_verified = models.BooleanField(default=False)
    def __str__ (self):
        return self.email
    
    def tokens(self):
        return ""


class PhoneNumber(models.Model):
    # phone =models.CharField(max_length=11) 
    # phone = PhoneNumberField(unique = True, null = True, blank = False) 
    phoneNumberRegex = RegexValidator(regex = r"^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\./0-9]*$")
    phoneNumber = models.CharField(validators = [phoneNumberRegex], max_length = 16, unique = True,null=True)
    user = models.ForeignKey(CustomUser,related_name="phoneNumber_user", on_delete=models.CASCADE)
    def __str__ (self):
        return self.phoneNumber
