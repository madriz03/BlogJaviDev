from django.urls import path
from post import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/<slug:slug>/', views.detail, name='detail'),
    path('post/<int:id>/<slug:slug>/add_comment/', views.add_comment, name='add_comment'),
    path('comment_delete/<int:id>/<slug:slug>/', views.comment_delete, name='delete')
    
    ]