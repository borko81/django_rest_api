from rest_framework import serializers
from .models import UserProfile


class ApiSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)


class ViewsetSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)


class UserProfileSerialzier(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = 'id email name password'.split()
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        user = UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user
