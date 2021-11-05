from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.validators import validate_email
from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, validated_data):
        user = authenticate(
            request=self.context['request'], email=validated_data['email'], password=validated_data['password'],
        )

        if not user:
            raise serializers.ValidationError('Incorrect email or password')

        return {'user': user}


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')
        extra_kwargs = {
            'password': {'required': True, 'write_only': True},
            'email': {'required': True},
        }

    def validate_email(self, email):
        validate_email(email)
        return email

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['email'],
            **validated_data,
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
