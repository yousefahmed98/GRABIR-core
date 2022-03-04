from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
router = DefaultRouter()
router.register("",views.PostViewset)


app_name = 'posts'

urlpatterns = [
    path('', include(router.urls))
]