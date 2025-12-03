from rest_framekork import serializers 
from .models import Unidade, Sala,  Status, Bem
class UnidadeSerializer(serializers.ModelsSerializer):
    class Meta:
        model = Unidade
        fields = "-all_"
class SalaSerializer(serializer.ModelsSerializer):
    class Meta:
        model = Sala
        fields = "__all__"
class StatusSerializer(serializers.ModelsSerializer):
    class Meta:
        model = Status
        fields = "__all__"
class Bemserializer(serializers.ModelsSerializer):
    class Meta:
        model = Bem
        fields = "__all__"