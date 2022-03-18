from django.contrib import admin

# Register your models here.

from GRABIR.apps.notification.models import Notification

# Register your models here.
admin.site.register(Notification)
