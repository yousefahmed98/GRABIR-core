from django.contrib import admin

from GRABIR.apps.payments.models import Payment, PaymentStatus

# Register your models here.
admin.site.register(Payment)
admin.site.register(PaymentStatus)