from rest_framework import serializers
from logbook.models import Student, Workweek


class WeekSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workweek
        fields = [
            'id', 
            'author', 
            'start_date', 
            'image', 
            'd1', 'd2', 'd3', 'd4', 'd5']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            'id', 
            'matric',
            'first_name',
            'last_name',
            'user_email',
            'start_date',]

