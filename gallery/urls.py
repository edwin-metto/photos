from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('profile/', views.profile, name='profile'),

    path('register/', views.register, name='register'),  
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),  
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),  
    path('upload/', views.upload_image, name='upload_image'),  
    path('images/', views.image_list, name='image_list'),  
    path('like/<int:image_id>/', views.like_image, name='like_image'),
    path('dislike/<int:image_id>/', views.dislike_image, name='dislike_image'),
    path('delete/<int:image_id>/', views.delete_image, name='delete_image'),



]
