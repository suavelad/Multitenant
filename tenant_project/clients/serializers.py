from rest_framework import serializers
from .models import Admin

class AdminUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'
