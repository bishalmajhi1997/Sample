from rest_framework import serializers
from .models import Student

#validators
def start_with_r(value):
    if value[0].lower() !="r":
        raise serializers.ValidationError('Name should be start with R')


class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=100,validators=[start_with_r])
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=100)

    def create(self,validate_data):
        return Student.objects.create(**validate_data)

    def update(self,instance,validated_data):
        print(instance.name)
        instance.name=validated_data.get('name',instance.name)
        print(instance.name)
        instance.roll=validated_data.get('roll',instance.roll)
        instance.city=validated_data.get('city',instance.city)
        instance.save()
        return instance

    #Validate
    def validate_roll(self,value):
        if value >=200:
            raise serializers.ValidationError("Seat Full")
        return value

    #OBJECT LEVEL VALIDATION
    def validate(self,data):
        nm=data.get("name")
        ct=data.get("city")
        if nm.lower()=="rohit" and ct.lower() != "ranchi":
            raise serializers.ValidationError("City must be Ranchi")
        return data
