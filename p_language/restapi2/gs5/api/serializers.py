from rest_framework import serializers
from .models import Student
# Validators
def starts_with_r(value):
    if value[0].lower() !="r":
        raise serializers.ValidationError("name should be started with r.")
class StudentSerializers(serializers.Serializer):
    # id=serializers.IntegerField()
    name=serializers.CharField(max_length=100,validators=[starts_with_r])
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=100)
    def __str__(self):
        return self.name
    
    def create(self,validated):
        return Student.objects.create(**validated)
    
    def update(self,instance,validated):
        print(instance.name)
        instance.name=validated.get("name",instance.name)
        instance.roll=validated.get("roll",instance.roll)
        instance.city=validated.get("city",instance.city)
        instance.save()
        return instance
    # Field_level validations
    def validate_roll(self,value):
        if value >=200:
            raise serializers.ValidationError("Seat Full")
        return value
    # Object =_level validations
    def validate(self,data):
        nm=data.get("name")
        ct=data.get("city")
        if nm.lower()=="rohit" and ct.lower() !="ranchi":
            raise serializers.ValidationError('City must be ranchi.')
        return data
    
