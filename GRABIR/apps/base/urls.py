
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
    path('email-receiver/', views.EmailReceiver, name="email-receiver"),
    path('login', views.LoginAPIView.as_view(), name="login"),
    path('request-reset-email/', views.RequestResetPassword.as_view(),
         name="request-reset-email"),
    path('set-pass/', views.SetNewPasswordAPIView.as_view(),
    name="set-pass"),
]