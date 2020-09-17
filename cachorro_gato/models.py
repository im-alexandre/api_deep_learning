from datetime import datetime

from django.db import models

# Create your models here.


def upload_location(instance, filename, **kwargs):
    agora = datetime.now().strftime('%h%m%s')
    file_path = f'imagens/{instance.id}_{agora}'
    return file_path


class Bicho(models.Model):
    """description"""
    imagem = models.ImageField(upload_to='instance', null=False, blank=False)
    # eh_cachorro = models.BooleanField(blank=True, null=True)
