from rest_framework import serializers
from budgetmeapi.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id',
                  'email',
                  'fname',
                  'lname',
                  'pwd')