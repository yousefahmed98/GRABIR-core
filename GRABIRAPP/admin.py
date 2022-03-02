from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser,Tag,Post,Offer,OfferStatus,Deal,PhoneNumber

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'is_staff','region','passport_img',)

    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
       
       
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),

        ('Additional info', {
            'fields': ('region','passport_img')
        }),
       
    )
    


class CustomTag(admin.ModelAdmin):
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'is_staff','region','passport_img',)

admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Offer)
admin.site.register(OfferStatus)
admin.site.register(PhoneNumber)
admin.site.register(Deal)