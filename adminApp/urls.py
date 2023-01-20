from django.urls import path, include
from . import views

urlpatterns = [
    path('dashboard/', views.getDashboard, name='dashboard'),
    path('categories/', views.viewCategories, name='view-categories')
]

##routes for category, view all categories, add category, delete category, edit category?   