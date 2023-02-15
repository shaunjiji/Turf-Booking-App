from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from . models import *
from django.http import HttpResponse
from .forms import BookingForm

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
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    userid = user.id
    if user is not None:
        login(request,user)
        request.session['username'] = username
        request.session['password'] = password 
        request.session['userid'] = userid
        return redirect('viewTurfs')
    else:
        print('incorrect login info')
        return render(request, 'signup.html')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('viewTurfs') 
    # redirect to user panels
    
    else:   
        return render (request, 'login.html')

    
def turf_view(request, id):
    data = Turfdb.objects.filter(id=id)
    form = BookingForm
    return render (request, 'turf.html', {'data': data, 'form': form, 'id': id })
    

def book_turf(request):
    if request.user.is_authenticated:  
        userid = request.session.get('userid')
        user = User.objects.get(id=userid)
        date = request.POST['date']
        time = request.POST['time']
        id = request.POST['turf']
        turf = Turfdb.objects.get(id=id)
        if Bookingdb.objects.filter(turfid=turf, date=date, time=time).exists():
            print('venue has already been booked for this time')
            return HttpResponse('venue has already been booked for this time')
        else:
            data = Bookingdb(userid=user,turfid=turf, date=date, time=time)
            data.save()
            return HttpResponse('reservation has been sent')
    else:
        return redirect ('login_view')

def logout(request):
    del request.session['username'] 
    del request.session['password']
    del request.session['userid'] 
    return render (request, 'login.html')

def bookings_view(request):
    if 'userid' in request.session:
        userid = request.session.get('userid')
        user = User.objects.get(id=userid)
        data = Bookingdb.objects.filter(userid=user)
        return render (request, 'bookings.html', {'data': data})
    else:
        return render (request, 'login.html')


##user can view his/her upcoming bookings, delete booking or edit booking
