from django.urls import path, include
from . import views

urlpatterns = [
    path('dashboard/', views.getDashboard, name='dashboard'),
    path('categories/', views.viewCategories, name='view-categories')
]

