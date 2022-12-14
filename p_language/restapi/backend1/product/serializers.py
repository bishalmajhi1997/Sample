from rest_framework import serializers
from .models import Product

# generics



# post
class ProductSerializers(serializers.ModelSerializer):
    my_discount=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=Product
        fields=["title",
        "content","price","sale_price","my_discount"]
    def get_my_discount(self,obj):
        # print(obj.id)
        if not hasattr(obj,"id"):
            return None
        if not isinstance(obj,Product):
            return None

        try:
            return obj.get_discount()
        except:
            return None


# get
# class ProductSerializers(serializers.ModelSerializer):
#     my_discount=serializers.SerializerMethodField(read_only=True)
#     class Meta:
#         model=Product
#         fields=["title",
#         "content","price","sale_price","my_discount"]
#     def get_my_discount(self,obj):
#         print(obj.id)
#         return obj.get_discount()