from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('posts/', views.getPosts, name="get_posts"),
    path('posts/<str:post_id>', views.getOnePost, name="get_one_posts"),
]
