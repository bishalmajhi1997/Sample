# Validations
# Field Level Validations
# Object Level Validations
# Validators


# FIELD LEVEL VALIDATIONS
# we can specify custom field-level validation by adding validate_fieldname methods should return the validated value or raise  a serializers.ValidationError
# Syntax:def validate_fieldname(self,value):
# Example:-def validate_roll(self,value):
                #   where,value is the field value that requires validation
from rest_framework import serializers
class StudentSerializers(serializers.Serializer):
    name=serializers.CharField(max_length=100)
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=100)

    def validate_roll(self,value):
        if value>=200:
            raise serializers.ValidationError("Seat Full")
        return value

# OBJECT LEVEL VALIDATIONS
# When we need to do validation that requires access to multiple fileds we do objects level validation by adding a method called validate() to serializer subclass.
# It raises a serializers.ValidationError if necessary or just return the validated values.
# Syntax:def validate(self,data):
# where ,data is a dictionary of field values.
def validate(self,data):
    nm=data.get('name')
    ct=data.get("city")
    if nm.lower()=="rohit" and ct.lower()!="ranchi":
        raise serializers.ValidationError("City must be ranchi.")
    return data

# VALIDATORS
# Most of times you are dealing with validation in REST FRAMEWORK you will simply be relying on the default field validation,or 
# writing explicit validation methods on serializer or field classes.
# However,sometimes you will want to place your validation logic into reusable compenents,so that it can easily be reused throughout your codebase.This can be acheived by using validator function and validator class.
def starts_with_r(value):
    if value[0].lower() !="r":
        raise serializers.ValidationError('Name must be started with R.')
class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=100,validators=[starts_with_r])
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=100)