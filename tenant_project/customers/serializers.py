from rest_framework import serializers
from .models import Userprofile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userprofile
        fields = '__all__'
