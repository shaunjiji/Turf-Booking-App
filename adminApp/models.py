from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

#manager table, category table, turf table

class Categorydb(models.Model):
    image = models.ImageField(upload_to='category')
    name = models.CharField(max_length=100)

class Managerdb(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    image = models.ImageField(upload_to='managers')
    password = models.CharField(max_length=20)
    
class Turfdb(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image =  models.ImageField(upload_to='turf')
    price = models.IntegerField() 
    location = models.CharField(max_length=100)
    categoryid = models.ForeignKey(Categorydb, on_delete=CASCADE)
    managerid = models.ForeignKey(Managerdb, on_delete=CASCADE)

