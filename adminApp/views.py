from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import *
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.

def getDashboard(request):
    return render(request, 'index.html')

def viewCategories(request):
    data = Categorydb.objects.all()
    return render(request, 'view-categories.html', {'data': data} )

def addCategories(request):
    if request.method == 'POST':
        name_u = request.POST['name']
        image_u = request.FILES['image']
        data = Categorydb(name = name_u, image = image_u)
        data.save()
        return redirect('viewCategories')

    elif request.method == 'GET':
        return render(request, 'add-categories.html')
    return render(request, 'add-categories.html')

def deleteCategory(request, id):
    Categorydb.objects.filter(id=id).delete()
    return redirect('viewCategories')

def updateCategory(request, id):
    if request.method == 'POST':
        name_u = request.POST['name']
        try:
            image_u = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(image_u.name, image_u)
        except MultiValueDictKeyError:
            file = Categorydb.objects.get(id=id).image

            Categorydb.objects.filter(id=id).update(name=name_u, image=file)
            return redirect('viewCategories')


def viewManagers(request):
    data = Managerdb.objects.all()
    return render(request, 'view-managers.html', {'data': data})

def addManager(request):
    if request.method == 'POST':
        name_u = request.POST['name']
        email_u = request.POST['email']
        password_u = request.POST['password']
        image_u = request.FILES['image']
        data = Managerdb(name = name_u, email = email_u, password = password_u, image = image_u)
        data.save()
        return redirect('viewManagers')

    elif request.method == 'GET':
        return render(request, 'add-managers.html')
    return render(request, 'add-managers.html')
       
def deleteManager(request, id):
    Managerdb.objects.filter(id=id).delete()
    return redirect('viewManagers')

def updateManager(request, id):
    if request.method == 'POST':
        name_u = request.POST['name']
        email_u = request.POST['email']
        password_u = request.POST['password']
        try:
            image_u = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(image_u.name, image_u)
        except MultiValueDictKeyError:
            file = Managerdb.objects.get(id=id).image

            Managerdb.objects.filter(id=id).update(name=name_u, email=email_u, password=password_u, image=file)
            return redirect('view')

def viewTurfs(request):
    data = Turfdb.objects.all()
    return render(request, 'view-turfs.html', {'data': data})


def addTurf(request):
    if request.method == 'POST':
        name_u = request.POST['name']
        description_u = request.POST['description']
        image_u = request.FILES['image']
        price_u = request.POST['price']
        location_u = request.POST['location']
        manager  = request.POST['managers']
        category = request.POST['categories']
        data = Turfdb(name=name_u, description=description_u, image=image_u, price=price_u, location=location_u, managerid=Managerdb.objects.get(id=manager), categoryid=Categorydb.objects.get(id=category))
        data.save()
        return redirect('viewTurfs')

    elif request.method == 'GET':
        managers = Managerdb.objects.all()
        categories = Categorydb.objects.all()
        return render(request, 'add-turfs.html', {'managers':managers, 'categories': categories})


def deleteTurf(request, id):
    Turfdb.objects.filter(id=id).delete()
    return redirect('viewTurfs')    
    



