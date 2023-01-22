from django.urls import path, include
from . import views

urlpatterns = [
    path('dashboard/', views.getDashboard, name='dashboard'),
    path('categories/', views.viewCategories, name='viewCategories'),
    path('add-category/', views.addCategories, name='addCategories'),
    path('delete-dategory/<int:id>', views.deleteCategory, name='deleteCategory')
]
 
