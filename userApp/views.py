from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from . models import *

# Create your views here.

def getHome(request):
    return render(request,'home.html')

def viewTurfs(request):
    data = Turfdb.objects.all()
    return render(request, 'turfs.thml', {'data': data})


def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
