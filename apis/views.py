from logbook.models import Workweek
from apis.serializers import WeekSerializer
from django.shortcuts import render
from rest_framework import generics

# Create your views here.

class StudentWeeks(generics.ListAPIView):
    serializer_class = WeekSerializer

    def get_queryset(self):
        """returns all the workweeks for a particular student"""
        student = self.request.user
        return Workweek.objects.filter(author=student)


class WeekUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = WeekSerializer

    def get_queryset(self):
        """returns all the workweeks for a particular student"""
        student = self.request.user
        return Workweek.objects.filter(author=student)

        


    