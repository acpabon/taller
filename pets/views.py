from django.shortcuts import render
from pets.models import Person, Mascot, Specie, Observation

from rest_framework import viewsets, permissions
from .serializers import MascotaSerializer, EspecieSerializer, ObservacionSerializer, PersonaSerializer

# Create your views here.
class MascotaViewSet(viewsets.ModelViewSet):
    queryset = Mascot.objects.all()
    serializer_class = MascotaSerializer
    permission_classes = [permissions.IsAuthenticated]

class EspecieViewSet(viewsets.ModelViewSet):
    queryset = Specie.objects.all()
    serializer_class = EspecieSerializer
    permission_classes = [permissions.IsAuthenticated]

class ObservacionViewSet(viewsets.ModelViewSet):
    queryset = Observation.objects.all()
    serializer_class = ObservacionSerializer
    permission_classes = [permissions.IsAuthenticated]

class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonaSerializer
    permission_classes = [permissions.IsAuthenticated]