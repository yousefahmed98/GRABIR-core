from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.getRoutes, name="routes"),
    
    # ------------------------Post------------------------
    path('posts/', views.getPosts, name="get_posts"),
    path('posts/<str:post_id>', views.getOnePost, name="get_one_post"),
    path('add-post', views.addPost, name='add_post'),
    path('edit-post/<str:post_id>', views.editPost, name='edit_post'),
    path('delete-post/<str:post_id>', views.deletePost, name='delete_post'),
    
    # ------------------------User-------------------------
    path('users/', views.getUsers, name="get_posts"),
    path('users/<str:user_id>', views.getOneUser, name="get_one_user"),
    path('add-user', views.addUser, name='add_post'),
    path('edit-user/<str:user_id>', views.editUser, name='edit_user'),
    path('delete-user/<str:user_id>', views.deleteUser, name='delete_user'),
]
