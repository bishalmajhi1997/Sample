from rest_framework import serializers
from .models import Student
# Validators
def starts_with_r(value):
    if value[0].lower() !="r":
        raise serializers.ValidationError("name should be started with r.")
class StudentSerializers(serializers.ModelSerializer):
    # id=serializers.IntegerField()
    name=serializers.CharField(max_length=100,validators=[starts_with_r])
    class Meta:
        model=Student
        fields=["name","roll","city"]
    # Field_level validations
    def validate_roll(self,value):
        if value >=200:
            raise serializers.ValidationError("Seat Full")
        return value
    # Object =_level validations
    def validate(self,data):
        nm=data.get("name")
        ct=data.get("city")
        if nm.lower()=="mohan" and ct.lower() !="ranchi":
            raise serializers.ValidationError('City must be ranchi.')
        return data
    
