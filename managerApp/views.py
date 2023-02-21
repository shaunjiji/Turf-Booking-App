from django.shortcuts import render
from adminApp.models import *

# Create your views here.

def manager_view(request):
    return render (request,'manager-login.html')

def manager_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        if Managerdb.objects.filter(email=email,password=password).exists():
            data = Managerdb.objects.filter(email=email, password=password).values('name', 'image').first()
            request.session['name'] = data['name']
            request.session['managerid'] = data['id']
            request.session['username'] = data['username']
            request.session['password'] = data['password']