from django.urls import path, include
from . import views

urlpatterns = [
    path('dashboard/', views.getDashboard, name='dashboard'),
    path('categories/', views.viewCategories, name='viewCategories'),
    path('add-category/', views.addCategories, name='addCategories'),
    path('delete-category/<int:id>', views.deleteCategory, name='deleteCategory'),
    path('update-category/<int:id>', views.updateCategory, name='updateCategory'),
    path('managers/', views.viewManagers, name='viewManagers'),
    path('delete-manager/<int:id>', views.deleteManager, name='deleteManager'),
    path('add-manager/', views.addManager, name='addManager'),
    path('update-manager/<int:id>', views.updateManager, name='updateManager'),

]
 
 