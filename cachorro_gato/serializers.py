from rest_framework import serializers

from .models import Bicho


class BichoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bicho
        fields = ['imagem']
