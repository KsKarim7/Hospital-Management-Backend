from rest_framework import serializers
from django.contrib.auth.models import User
from . import models

class PatientSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    class Meta:
        model = models.Patient
        fields = '__all__' 

class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required = True)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password','confirm_password']

    def save(self):
        username = self.validated_data['username']
        email = self.validated_data['email']
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': "This mail is already in use! "})

        account = User(username = username, email = email)
        print(account)
        account.set_password(password)
        account.save()
        return account