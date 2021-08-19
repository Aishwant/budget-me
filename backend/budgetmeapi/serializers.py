from rest_framework import serializers
from budgetmeapi.models import BudgetMeAPI

class BudgetMeAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = BudgetMeAPI
        fields = ('id',
                    'title',
                    'description',
                    'published')