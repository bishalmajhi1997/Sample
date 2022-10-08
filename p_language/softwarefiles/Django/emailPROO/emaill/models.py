from django.db import models

# Create your models here.
from django.contrib.auth.models import User
# Create your models here.
class User(models.Model):
    email=models.CharField(max_length=200)
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=200)
