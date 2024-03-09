from .models import Account
from rest_framework import serializers

class AccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = Account
        fields = '__all__'