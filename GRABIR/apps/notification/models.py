from django.db import models
from GRABIR.apps.base.models import CustomUser

class Notification(models.Model):
    class Meta:
        ordering = ['pk']
    body = models.CharField(max_length=50)
    from_user= models.ForeignKey(CustomUser,related_name="from_user", on_delete=models.CASCADE)
    to_user= models.ForeignKey(CustomUser,related_name="to_user", on_delete=models.CASCADE)
    from_user_name = models.CharField(null=True,max_length=50)
    from_user_ProfilePic = models.FileField(upload_to='images/', null=True, verbose_name="Owner Picture")
    

    def __str__(self):
        return self.body + ' | ' + str(self.from_user)
