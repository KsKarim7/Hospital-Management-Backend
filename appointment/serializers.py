from rest_framework import serializers
from . import models


class AppointmentSerializer(serializers.ModelSerializer):
    time = serializers.StringRelatedField(many=False)  # 1 appointment has 1 time filed
    patient = serializers.StringRelatedField(many=False)  # 1 appointment has 1 time filed
    doctor = serializers.StringRelatedField(many=False)  # 1 appointment has 1 time filed

    class Meta:
        model = models.Appointment
        fields = '__all__'