from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:id>', views.detail, name='detail')
    
]