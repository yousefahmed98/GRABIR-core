from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
router = DefaultRouter()
router.register("notifications",views.NotificationViewset)


app_name = 'notification'

urlpatterns = [
    path('', include(router.urls))
]