from rest_framework import serializers
from .models import Mascot, Specie, Observation, Person

class EspecieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specie
        fields = '__all__'

class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascot
        fields = '__all__'

class ObservacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Observation
        fields = '__all__'

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
