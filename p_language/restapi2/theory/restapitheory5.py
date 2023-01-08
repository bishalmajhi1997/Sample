# MODELSERIALIZER CLASS
# The modelserialzier class provides a shortcut that lets you automatically create a serailizer class with fields
# that correspond to the model fields.
# The modelserializer class is same as a regular serializer class,except that:
# it will automatically generate  a set of fields for you,based on the model.
# it will automatically generate validators for the serailizer,such as unique_together validators.
# it includes simple default implementation of create() and update().

# eg:
# from rest_framework import serializers
# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Student
#         fields=["id","name","roll","city"]
# fields="__all__"
# exclude=["roll"]

# core arguments
# class StudentSerializer(serializers.ModelSerializer):
    # name=serializers.CharField(read_only=True)
#     class Meta:
#         model=Student
#         fields=["id","name","roll","city"]

# or
# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Student
#         fields=["id","name","roll","city"]
#         read_only_fields=['name','roll'],

     
# modelserializers validators
# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Student
#         fields=["id","name","roll","city"]
#    def validate_roll(self,value):
        #  if value>=200:
            #    raise serializers.ValidationError('Seat full ')
            # return value
