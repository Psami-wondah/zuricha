# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('logout/', views.logout_request, name='logout'),
    path('login/', views.login_request, name='login'),
    path('register/', views.signup, name='register'),
    path('', views.index, name='index'),
    path('chat/<str:room_name>/', views.room, name='room'),
]