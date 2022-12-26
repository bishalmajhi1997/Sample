from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from address.models import AddressField


# Create your models here.
# create a project by name project2 and app by name app2
# create a model by name user with a fields-first_name,last_name,email
# create a view by name user and display the user details on users.html template in the form of lists.
class User(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=30,unique=True)
    def __str__(self):
        return self.email

# model-Student-name,age,contact,address
# views-student_form
# form=student_form
class Student(models.Model):
    name=models.CharField(max_length=50,blank=True)
    age= models.PositiveIntegerField(null=False, blank=False)
    contact=PhoneNumberField(unique = True, null = False, blank = False) 
    address =models.TextField(blank=True,max_length=100)
    def __str__(self):
        return str(self.contact)

