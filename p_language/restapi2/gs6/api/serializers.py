from rest_framework import serializers
from .models import Student
class StudentSerializers(serializers.ModelSerializer):
    # id=serializers.IntegerField()
    class Meta:
        model=Student
        fields=["name","roll","city"]
    
    
