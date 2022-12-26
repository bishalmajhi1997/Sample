from rest_framework import serializers
class StudentSerializers(serializers.Serializer):
    id=serializers.IntegerField()
    name=serializers.CharField()
    roll=serializers.IntegerField()
    city=serializers.CharField()
