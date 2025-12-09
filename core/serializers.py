# ...existing code...
from rest_framework import serializers
from .models import Unidade, Sala, Status, Bem

class UnidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unidade
        fields = "__all__"

class SalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sala
        fields = "__all__"

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = "__all__"

class BemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bem
        fields = "__all__"
# ...existing code...