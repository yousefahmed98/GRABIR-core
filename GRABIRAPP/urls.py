from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.getRoutes, name="routes"),
    
    # ------------------------Post------------------------
    path('posts/', views.getPosts, name="get_posts"),
    path('posts/<str:post_id>', views.getOnePost, name="get_one_posts"),
    path('add-post', views.addPost, name='add_post'),
    path('edit-post/<str:post_id>', views.editPost, name='edit_post'),
    path('delete-post/<str:post_id>', views.deletePost, name='delete_post'),

]
