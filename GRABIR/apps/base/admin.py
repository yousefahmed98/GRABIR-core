from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from phonenumbers import PhoneNumber
from GRABIR.apps.base.models import CustomUser

# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'is_staff','region','passport_img',"ProfilePic")

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
            'fields': ('region','passport_img','ProfilePic')
        }),

        
       
    )
    

class CustomTag(admin.ModelAdmin):
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'is_staff','region','passport_img',"ProfilePic")



admin.site.register(CustomUser,CustomUserAdmin)
