from django.shortcuts import render
from rest_framework import viewsets
from . import serializers
from . import models

# Create your views here.
class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = models.Appointment.objects.all()
    serializer_class = serializers.AppointmentSerializer


    #custom query
    def get_queryset(self):
        queryset = super().get_queryset()  # Inheriting parent class from 7th line
        patient_id = self.request.query_params.get('patient_id')
        if(patient_id):
            queryset = queryset.filter(patient_id=patient_id)
        return queryset