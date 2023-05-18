from django.urls import path
from . import views






urlpatterns = [
   
    path('Post/', views.Post, name='post'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    
]
 