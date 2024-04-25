from rest_framework import serializers
from .models import Course

class CourseSerializaer(serializers.Serializer):
    class Meta: 
        model = Course
        fields = '__all__'