
from django.contrib import admin , auth
from django.urls import path , include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import TemplateView
from . import views
from .views import projet_details_csv , logout_view
from artyprod.views import submit_review
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect





urlpatterns = [
    
    path('', views.home, name='home'), 
    path('register/', views.register, name='register'),
    path('login/',views.login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('portfolio_view/',views.portfolio_view, name = 'portfolio_view'),
    path('project_request/', views.project_request, name='project_request'),
    path('my_projects/', views.my_projects, name='my_projects'),
    path('project_details/<int:pk>/', views.project_details, name='project_details'),
    path('contact',views.contact, name='contact'),
    path('equipe_view', views.personnel_view, name='equipe_view'),
    path('projet/<int:projet_id>/details/csv/', views.projet_details_csv, name='projet_details_csv'),
    path('submit_review/', submit_review, name='submit_review'),
    
    



]
    
   
    
