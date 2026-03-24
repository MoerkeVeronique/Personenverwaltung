from django.contrib.auth.models import User
from rest_framework import serializers
from mitarbeiter.models import Mitarbeiter

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email']

class MitarbeiterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mitarbeiter
        fields = '__all__'