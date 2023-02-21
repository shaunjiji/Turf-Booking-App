from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.manager_view, name='login_view'),
    path('login_manager/',views.manager_login, name='manager-login')
]
 
 