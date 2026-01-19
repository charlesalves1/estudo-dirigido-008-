from rest_framework import serializers
from .models import Unidade, Sala, Status, Bem, Categoria


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
        fields = (
            "id",
            "nome",
            "tombo",
            "unidade",
            "sala",
            "status",
            "categoria",
            "criado_em",
            "atualizado_em",
        )

    def validate(self, data):
        status = data.get("status")
        sala = data.get("sala")

        # Regra 1: bem ativo precisa ter sala
        if status and status.nome.lower() == "ativo" and not sala:
            raise serializers.ValidationError(
                "Um bem com status 'Ativo' deve estar associado a uma sala."
            )

        return data



class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"