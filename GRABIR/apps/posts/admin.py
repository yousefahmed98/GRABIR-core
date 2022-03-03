from django.contrib import admin

from GRABIR.apps.posts.models import Post, Tag

# Register your models here.
admin.site.register(Tag)
admin.site.register(Post)