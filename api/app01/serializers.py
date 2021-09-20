from rest_framework import serializers
from .models import University, Student


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):

    university_name = serializers.CharField(source='university.name')

    class Meta:
        model = Student
        fields = '__all__'
