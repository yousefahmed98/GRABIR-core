"""GRABIR URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from GRABIR.apps.base import urls  as base_urls
from GRABIR.apps.base.views import RestPasswordTokenCheckAPI, VerifyEmail
from GRABIR.apps.deals import urls as deals_urls
from GRABIR.apps.offers import urls as offers_urls
from GRABIR.apps.payments import urls as payments_urls
from GRABIR.apps.posts import urls as posts_urls
from GRABIR.apps.rate import urls as rate_urls
from GRABIR.apps.notification import urls as notification_urls
# for post image
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('auth', obtain_auth_token),
    path('admin/', admin.site.urls),
    path('base/', include( base_urls, namespace='base')),
    path('deals/', include( deals_urls, namespace='deals')),
    path('offers/', include( offers_urls, namespace='offers')),
    path('posts/', include( posts_urls, namespace='posts')),
    path('payments/', include( payments_urls, namespace='payments')),
    path('rate/', include( rate_urls, namespace='rate')),
    path('password-reset/<uidb64>/<token>/',
        RestPasswordTokenCheckAPI.as_view(), name='password-reset-confirm'),
    
    path('notification/', include( notification_urls, namespace='notification')),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
