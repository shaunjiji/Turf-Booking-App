from django.shortcuts import render

# Create your views here.

def getHome(request):
    return render(request,'home.html')