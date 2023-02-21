from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.manager_view, name='login_view'),
    path('login_manager/',views.manager_login, name='manager-login'),
    path('requests/', views.manager_requests, name='requests'),
    path('approve/<int:id>', views.approve_request, name='approve-request')
]
 
 