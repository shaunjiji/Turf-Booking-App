from django.urls import path, include
from . import views

urlpatterns = [
    path('home/',views.getHome, name='home'),
    path('turfs/', views.viewTurfs, name='viewTurfs')

]
 
 