from rest_framework import serializers
from api.models import Expense
class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Expense
        fields=["date","description","amount","category"]
