from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import UserProfile


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "password")
        extra_kwargs = {
            "password": {"write_only": True}  
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()    


class UserProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)
    email = serializers.EmailField(source="user.email", read_only=True)

    class Meta:
        model = UserProfile
        fields = [
            "id",
            "username",
            "email",
            "gender",
            "date_of_birth",
            "profile_picture",
            "preferences",
            "created_at",
            "updated_at"
        ]
        read_only_fields = ["created_at", "updated_at"]


        

        