from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from JoinApp.api.serializers import ContactSerializer
from user_auth_app.models import Account



class AccountSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True, required=True)

    class Meta(ContactSerializer.Meta):
        model = Account
        fields = ["id", "name", "email", "tel", "password"]

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data["password"])  # Passwort hashen
        return super().create(validated_data)   
    
    # def update(self, instance, validated_data):
    #     if "password" in validated_data:
    #         validated_data["password"] = make_password(validated_data["password"])
    #     return super().update(instance, validated_data)
