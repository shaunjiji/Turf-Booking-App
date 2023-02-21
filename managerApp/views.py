from django.shortcuts import render, redirect
from adminApp.models import *

# Create your views here.

def manager_view(request):
    return render (request,'manager-login.html')

def manager_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        if Managerdb.objects.filter(email=email,password=password).exists():
            data = Managerdb.objects.filter(email=email, password=password).values('name','id').first()
            request.session['name'] = data['name']
            request.session['managerid'] = data['id']
            request.session['email'] = email
            request.session['password'] = password
            return render (request, 'manager-index.html')
        else:
            return redirect(manager_view)