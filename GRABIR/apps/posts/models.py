from django.db import models

from GRABIR.apps.base.models import CustomUser


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
    # created_at = models.DateField(auto_now_add=True,null=True)
    # updated_at = models.DateTimeField(auto_now=True,null=True)
    from_region= models.CharField(null=True,max_length=50)
    to   = models.CharField(null=True,max_length=50)
    tags = models.ManyToManyField(Tag, through='PostTags')
    user = models.ForeignKey(CustomUser,related_name="post_user", on_delete=models.CASCADE)
    price = models.FloatField(null=True)

    
    def show_tags(self):
        return "\n".join([a.name for a in self.tags.all()])

    def __str__(self):
        return self.title + ' | ' + str(self.user)



class PostTags(models.Model):
    post = models.ForeignKey(Post,related_name="postTags_post", on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, related_name="postTags_tag", on_delete=models.CASCADE)
