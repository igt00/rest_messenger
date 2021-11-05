from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.validators import validate_email
from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, validated_data):
        user = get_user_model().objects.filter(email=validated_data['email'])

        if not user:
            raise serializers.ValidationError('Invalid email')

        user = user.get()
        if not user.check_password(validated_data['password']):
            raise serializers.ValidationError('Invalid password')

        return {'user': user}


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = settings.AUTH_USER_MODEL
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
