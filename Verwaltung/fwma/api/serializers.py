from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, serializers
from mitarbeiter.models import Mitarbeiter, Qualifikation

# Create your views here.

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'  

class MitarbeiterSerializer(serializers.ModelSerializer):
    qualifikationen = serializers.SerializerMethodField()  
    
    class Meta:
        model = Mitarbeiter
        fields = [
            'id', 'vorname', 'nachname', 'email', 'telefonnummer', 
            'qualifikationen'
        ]
    
    def get_qualifikationen(self, obj):
        return [mq.qualifikation.name for mq in obj.mitarbeiterqualifikation_set.all()]