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

    # ------------------------Offer------------------------
    path('offers/', views.getOffers, name='get_offers'),
    path('offer/<str:offer_id>', views.getOneOffer, name="get_one_offer"),
    path('add-offer', views.addOffer, name='add_offer'),
    path('edit-offer/<str:offer_id>', views.editOffer, name='edit_offer'),
    path('delete-offer/<str:offer_id>', views.deleteOffer, name='delete_offer'),

   # ------------------------Tags------------------------
    path('tags/', views.getTags, name='get_tags'),
    path('tags/<str:tag_id>', views.getOneTag, name="get_one_tag"),
    path('add-tag', views.addTag, name='add_tag'),
    path('edit-tag/<str:tag_id>', views.editTag, name='edit_tag'),
    path('delete-tag/<str:tag_id>', views.deleteTag, name='delete_tag'),

    # ------------------------Phone------------------------
    path('phones/', views.getPhones, name='get_phones'),
    path('phones/<str:phone_id>', views.getOnePhone, name="get_one_phone"),
    path('add-phone', views.addPhone, name='add_phone'),
    path('edit-phone/<str:phone_id>', views.editPhone, name='edit_phone'),
    path('delete-phone/<str:phone_id>', views.deletePhone, name='delete_phone'),


]

