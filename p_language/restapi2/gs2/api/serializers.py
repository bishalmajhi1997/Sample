from rest_framework import serializers
from .models import Student
class StudentSerializers(serializers.Serializer):
    # id=serializers.IntegerField()
    name=serializers.CharField()
    roll=serializers.IntegerField()
    city=serializers.CharField()
    def __str__(self):
        return self.name
    def create(self,validate_data):
        return Student.objects.create(**validate_data)