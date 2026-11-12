from django.urls import path
from . import views

urlpatterns = [
    path('',views.dashboard,name = 'dashboard'),
    path('categories/',views.categories,name = 'categories'),
    path('categories/add/',views.add_categories,name = 'add_categories'),
    path('categories/edit/<int:pk>',views.edit_category,name = 'edit_category'),
    path('categories/delete/<int:pk>',views.delete_category,name = 'delete_category'),
    # posts
    path('posts/',views.posts,name = "posts"),
    path('posts/add/',views.add_posts,name = 'add_posts'),
    path('posts/edit/<int:pk>',views.edit_posts,name = 'edit_posts'),
    path('posts/delete/<int:pk>',views.delete_posts,name = 'delete_posts'),
    # /users
    path('users/',views.users,name ="users"),
     path('users/add/',views.add_users,name = 'add_users'),

        
]