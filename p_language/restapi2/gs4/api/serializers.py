from rest_framework import serializers
from .models import Student
class StudentSerializers(serializers.Serializer):
    # id=serializers.IntegerField()
    name=serializers.CharField()
    roll=serializers.IntegerField()
    city=serializers.CharField()
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
    
