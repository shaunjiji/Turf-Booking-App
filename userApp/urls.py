from django.urls import path, include
from . import views

urlpatterns = [
    path('home/',views.getHome, name='home'),
    path('turfs/', views.viewTurfs, name='viewTurfs'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login')

]
 
 