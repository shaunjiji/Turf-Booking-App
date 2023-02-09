from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from . models import *

# Create your views here.

def getHome(request):
    return render(request,'home.html')

def viewTurfs(request):
    data = Turfdb.objects.all()
    return render(request, 'turfs.html', {'data': data})

def register(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(email=email).exists():
                print('Email has been taken')
            elif User.objects.filter(username=username).exists():
                print('Username has been taken')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password1)
                user.save()
                print('user created')
                return redirect('viewTurfs')
        else:
            print('Passwords do not match')
        return render(request, 'signup.html')

def signin(request):
    if request.user.is_authenticated:
        return render(request, 'turfs.html')
    else:
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request,user)
            print('user logged in')
            return render(request, 'turfs.html')
        else:
            print('incorrect login info')
            return render(request, 'signup.html')

def login_view(request):
    if request.method == 'GET':   
        return render (request, 'login.html')

    
def turf_view(request, id):
    data = Turfdb.objects.filter(id=id)
    return render (request, 'turf.html', {'data': data})
    



##user can book a turf, must be signed in and autheticated in order to do so. checks to see if turf is available for that timeslot
##user needs to be able to logout
##user can view his/her upcoming bookings, delete booking or edit booking
