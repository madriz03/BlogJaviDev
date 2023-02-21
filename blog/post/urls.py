from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('detail/<int:id>', views.detail, name='detail'),
    path('post/<int:id>/add_comment/', views.add_comment, name='add_comment')
    
]