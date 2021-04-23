from django.db import models

# Create your models here.
class Vaccine(models.Model):
    vaccine = models.CharField(max_length=100)

    def __str__(self):
        return self.vaccine

class Person(models.Model):
    lastName = models.CharField(max_length=100)
    firstName = models.CharField(max_length=100)
    contact = models.IntegerField()
    brgy = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    houseno = models.IntegerField()
    city = models.CharField(max_length=100)
    age = models.IntegerField()
    birth = models.DateField()
    vaccine = models.ForeignKey(Vaccine, on_delete=models.CASCADE)

    def __str__(self):
        return self.lastName