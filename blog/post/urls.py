from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('detail/<int:id>', views.detail, name='detail'),
    path('post/<int:id>/add_comment/', views.add_comment, name='add_comment'),
    path('comment_delete/<int:id>', views.comment_delete, name='delete'),
    path('login/', auth_views.LoginView.as_view(template_name='post/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name=('logout'))

    
]