from django.db import models

# Create your models here.
class Flight(models.Model):
    flightNumber=models.CharField(max_length=10)
    operatingAirlines=models.CharField(max_length=10)
    departurecity=models.CharField(max_length=20)
    arrivalcity=models.CharField(max_length=20)
    dateOfDeparture=models.DateField()
    estimateTimeofDeparture=models.TimeField()

class Passenger(models.Model):
    firstname=models.CharField(max_length=10)
    middlename=models.CharField(max_length=10)
    email=models.EmailField()
    mobileNo=models.CharField(max_length=10)

class Reservation(models.Model):
    flight=models.ForeignKey(Flight,on_delete=models.CASCADE)
    passenger = models.OneToOneField(Passenger, on_delete=models.CASCADE)

