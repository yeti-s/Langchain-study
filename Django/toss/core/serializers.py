from .models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False)
    age = serializers.IntegerField(required=False)
    sex = serializers.CharField(required=False)
    # secret
    password = serializers.CharField(write_only=True)
    is_staff = serializers.BooleanField(write_only=True)
    is_superuser = serializers.BooleanField(write_only=True)
    
    class Meta:
        model = User
        fields = '__all__'
        