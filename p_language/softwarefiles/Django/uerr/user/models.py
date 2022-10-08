from django.db import models

# Create your models here.
#from django.contrib.auth.models import User

from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
#    email=models.EmailField(max_length=254)
    def __str__(self):
        return self.User.username
