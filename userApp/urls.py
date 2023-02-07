from django.urls import path, include
from . import views

urlpatterns = [
    path('home/',views.getHome, name='home'),
    path('turfs/', views.viewTurfs, name='viewTurfs'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register')

]
 
 