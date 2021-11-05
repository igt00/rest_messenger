from rest_framework import serializers

from auth_system.models import User2


class User2Serializer(serializers.ModelSerializer):
    email = serializers.CharField(source='user.email', read_only=True)

    class Meta:
        model = User2
        fields = ('id', 'first_name', 'surname', 'second_name', 'email', 'gender')
