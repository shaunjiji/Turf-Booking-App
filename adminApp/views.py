from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import *

# Create your views here.

def getDashboard(request):
    return render(request, 'index.html')

def viewCategories(request):
    data = Categorydb.objects.all()
    return render(request, 'view-categories.html', {'data': data} )

