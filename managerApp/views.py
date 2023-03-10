from django.shortcuts import render, redirect
from adminApp.models import *
from userApp.models import *

# Create your views here.

def manager_view(request):
    if 'managerid' in request.session:
        return redirect(manager_requests)
    else:
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
            return redirect (manager_requests)
        else:
            return redirect(manager_view)
        
def manager_requests(request):
    if request.method == 'GET':
        if 'managerid' in request.session:
            managerid = request.session['managerid']
            turf = Turfdb.objects.filter(managerid=managerid).first()
            turfid = turf.id
            bookings = Bookingdb.objects.filter(turfid=turfid, status='Pending')
            return render (request, 'requests.html', {'bookings': bookings})
        else:
            return render('manager-login.html')
        
def approve_request(request, id):
    if request.method == 'GET':
        if 'managerid' in request.session:
            booking = Bookingdb.objects.get(id=id)
            booking.status = 'Approved'
            booking.save()
            return redirect(manager_requests)
        else:
            return redirect(manager_view)
    else:
        return redirect(manager_view)
    
def manager_logout(request):
    del request.session['name']
    del request.session['managerid']
    del request.session['email']
    del request.session['password'] 
    return render(request, 'manager-login.html')