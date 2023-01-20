from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import *

# Create your views here.

def getDashboard(request):
    return render(request, 'index.html')

def addCategories(request):
    if request.method == 'POST':
        name_u = request.POST['name']
        image_u = request.FILES['image']
        data = Categorydb(name = name_u, image = image_u)
        data.save()
        return redirect('viewCategories')
    
    return render(request, 'add-categories.html')

def viewCategories(request):
    data = Categorydb.objects.all()
    return render(request, 'view-categories.html', {'data': data} )

