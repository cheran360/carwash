from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.email

class Service(models.Model):
    location = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return str(self.id)
        
class Booking(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Success', 'Success'),
        ('Rejected', 'Rejected'),
    )
    customer_details = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    service_details = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.id)


