from django.urls import path
from post import views


urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:id>', views.detail, name='detail'),
    path('post/<int:id>/add_comment/', views.add_comment, name='add_comment'),
    path('comment_delete/<int:id>', views.comment_delete, name='delete')
    
    ]