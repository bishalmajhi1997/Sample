from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User

# Create your models here.
class StudentInformation(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=50,blank=True)
    age= models.PositiveIntegerField(null=False, blank=False)
    contact=PhoneNumberField(unique = True, null = False, blank = False) 
    address =models.TextField(blank=True,max_length=100)
    def __str__(self):
        return str(self.contact)
