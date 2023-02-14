from django.db import models
from django.db.models.deletion import CASCADE
from adminApp.models import Turfdb 
from django.contrib.auth.models import User
from datetime import datetime


TIME_CHOICES = (
    ("3 PM", "3 PM"),
    ("3:30 PM", "3:30 PM"),
    ("4 PM", "4 PM"),
    ("4:30 PM", "4:30 PM"),
    ("5 PM", "5 PM"),
    ("5:30 PM", "5:30 PM"),
    ("6 PM", "6 PM"),
    ("6:30 PM", "6:30 PM"),
    ("7 PM", "7 PM"),
    ("7:30 PM", "7:30 PM"),
    ("8:00 PM", "8:00 PM"),
    ("8:30 PM", "8:30 PM"),
    ("9:00 PM", "9:00 PM"),
    ("9:30 PM", "9:30 PM"),
    ("10:00 PM", "10:00 PM"),
    ("10:30 PM", "10:30 PM"),
    ("11:00 PM", "11:00 PM"),
)

PENDING = 0
APPROVED = 1
STATUS_CHOICES = (
    (PENDING, 'Pending'),
    (APPROVED, 'Approved'),
)

class Bookingdb(models.Model):
    userid = models.ForeignKey(User, on_delete=CASCADE)
    turfid = models.ForeignKey(Turfdb, on_delete=CASCADE)
    date = models.DateField()
    time = models.CharField(max_length=100,choices=TIME_CHOICES)
    time_booked = models.DateTimeField(default=datetime.now)
    status = models.CharField(max_length=100,choices= STATUS_CHOICES, default='Pending')


