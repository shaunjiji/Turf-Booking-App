from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from . models import *

# Create your views here.

def getHome(request):
    return render(request,'home.html')

def viewTurfs(request):
    data = Turfdb.objects.all()
    return render(request, 'turfs.html', {'data': data})

def signup(request):
    return render(request, 'signup.html')

def register(request):
    if request.method == 'POST':
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
        return redirect('signup')

def login(request):
    return render (request, 'login.html')



##user can book a turf, must be signed in and autheticated in order to do so. checks to see if turf is available for that timeslot
##user needs to be able to logout
##user can view his/her upcoming bookings, delete booking or edit booking
