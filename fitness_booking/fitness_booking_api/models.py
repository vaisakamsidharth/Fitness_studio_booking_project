from django.db import models

# Create your models here.

# Returns a list of all upcoming classes

class FitnessClass(models.Model):
    name = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)
    datetime = models.DateTimeField()
    available_slots = models.PositiveIntegerField()

class Booking(models.Model):
    # this field is used for returns all booking made by a specific mail addresss
    fitness_class = models.ForeignKey(FitnessClass, on_delete=models.CASCADE)
    # accepts booking requests fields
    client_name = models.CharField(max_length=100)
    client_email = models.EmailField()
    booking_time = models.DateTimeField(auto_now_add=True)
