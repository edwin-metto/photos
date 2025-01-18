from django.urls import path
from . import views  
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.image_list, name='image_list'),  
    path('upload/', views.upload_image, name='upload_image'), 
    path('like/<int:image_id>/', views.like_image, name='like_image'),  
    path('dislike/<int:image_id>/', views.dislike_image, name='dislike_image'),
     path('delete/<int:image_id>/', views.delete_image, name='delete_image'),
    path('register/', views.register, name='register'),  
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),  
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  
    path('profile/', views.profile, name='profile'),  
]
