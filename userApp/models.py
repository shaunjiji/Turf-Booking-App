from django.db import models
from django.db.models.deletion import CASCADE
from managerApp.models import Turfdb 

# Create your models here.
##user table, login, password
##bookings table
##

class Userdb(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=100)

class Bookingdb(models.Model):
    userid = models.ForeignKey(Userdb, on_delete=CASCADE)
    turfid = models.ForeignKey(Turfdb, on_delete=CASCADE)
    date = models.DateField()
    time = models.TimeField()

