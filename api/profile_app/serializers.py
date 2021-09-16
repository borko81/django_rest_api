from rest_framework import serializers


class ApiSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)