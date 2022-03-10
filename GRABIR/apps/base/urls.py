
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
router = DefaultRouter()
router.register("users",views.UserViewset)

app_name = 'base'

urlpatterns = [
    path('', include(router.urls)),
    path('register/', views.RegisterView.as_view(), name="register"),
    path('email-verify/', views.VerifyEmail, name="email-verify"),  

]