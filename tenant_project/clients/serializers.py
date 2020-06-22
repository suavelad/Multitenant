from rest_framework import serializers
from .models import Admin, Client,Domain

class AdminUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domain
        fields = '__all__'