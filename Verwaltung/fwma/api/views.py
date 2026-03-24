from .serializers import UserSerializer, MitarbeiterSerializer
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from mitarbeiter.models import Mitarbeiter

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class MitarbeiterViewSet(viewsets.ModelViewSet):
    queryset = Mitarbeiter.objects.all()
    serializer_class = MitarbeiterSerializer
    permission_classes = [permissions.IsAuthenticated] 