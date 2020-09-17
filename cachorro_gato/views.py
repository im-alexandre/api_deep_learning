import os

from django.core.files.storage import default_storage
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from .cnn_previsao_func import classifica
from .models import Bicho
from .serializers import BichoSerializer


# Create your views here.
@api_view([
    'POST',
])
def api_classifica(request):
    """view para classificar imagens"""
    if request.method == 'POST':
        f = request.FILES['imagem']
        response = {}
        file_name = "pic.jpg"
        file_name_2 = default_storage.save(file_name, f)
        eh_cachorro = (classifica(file_name_2)[0][0] == 1)
        os.remove(file_name_2)

        if eh_cachorro:
            resposta = 'cachorro'
        else:
            resposta = 'gato'
        return Response({'classifica': resposta})
