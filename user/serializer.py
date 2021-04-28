from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from user.models import User


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, min_length=8, write_only=True)
    access = serializers.CharField(max_length=255, read_only=True)
    refresh = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ('email', 'name', 'password', 'access', 'refresh',)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    name = serializers.CharField(max_length=255, read_only=True)
    access = serializers.CharField(max_length=255, read_only=True)
    refresh = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)

        if email is None:
            raise serializers.ValidationError('An email address is required to log in.')
        if password is None:
            raise serializers.ValidationError('A password is required to log in.')

        user = authenticate(email=email, password=password)

        if user is None:
            raise serializers.ValidationError('A user with this email and password was not found.')

        # if not user.is_active:
        #     raise serializers.ValidationError('This user has been deactivated.')

        return {'access': user.access, 'refresh': user.refresh}


class UserSerialiser(ModelSerializer):
    email = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = ('email', 'name', 'created_at', 'updated_at')


class UserReadSerialiser(ModelSerializer):
    email = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = ('email', 'name', 'created_at', 'updated_at')