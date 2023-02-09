from django.urls import path, include
from . import views

urlpatterns = [
    path('home/',views.getHome, name='home'),
    path('turfs/', views.viewTurfs, name='viewTurfs'),
    path('signin/', views.signin, name='signin'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login_view'),
    path('turf/<int:id>', views.turf_view, name='viewTurf')

]
 
 