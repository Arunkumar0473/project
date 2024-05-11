# hostel/models.py

# hostels/models.py
from django.db import models
from django.contrib.auth.models import User


class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)



# class Room(models.Model):
#     hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE)
#     room_number = models.CharField(max_length=10)
#     price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
#     capacity = models.IntegerField(default='DEFAULT_CODE')   # Set default capacity value
    # Add more fields as needed

    # Add more fields as needed

# class Booking(models.Model):
#     room = models.ForeignKey(Room, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     check_in_date = models.DateField(default='DEFAULT_CODE')
#     check_out_date = models.DateField(default='DEFAULT_CODE')
    # Add more fields as needed
class Member(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

class CustomerSupport(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=15)  # Changed to CharField to store phone numbers as strings
    message = models.CharField(max_length=255)
    
class sharing_type(models.Model):
    sharings=models.CharField(max_length=100,primary_key=True)
    def __str__(self):
        return self.sharings
class booking(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(primary_key=True)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)  # Assuming international format
    sharing_type =models.ForeignKey(sharing_type,on_delete=models.SET_NULL,null=True) # Adjust max length as necessary

    def __str__(self):
        return self.full_name 
class Payment(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    card_name = models.CharField(max_length=100)
    card_number = models.CharField(max_length=19)
    exp_month = models.CharField(max_length=20)
    exp_year = models.CharField(max_length=4)
    cvv = models.CharField(max_length=4)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.full_name} - {self.amount} - {self.transaction_date}-{self.email}-{self.card_name}" 
# Create your models here.
