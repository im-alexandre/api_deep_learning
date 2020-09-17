import os
from io import StringIO

import numpy as np
from keras.models import load_model
from keras.preprocessing import image
from PIL import Image

from django.core.files.base import ContentFile


def classifica(imagem):
    """função para classificar cachorros e gatos"""
    cnn = load_model("cachorro_gato/cnn.h5")
    test_image = image.load_img(imagem, target_size=(64, 64))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)
    eh_cachorro = cnn.predict(test_image)
    return eh_cachorro


if __name__ == '__main__':
    path = os.path.join(
        '/home/alexandre/Cursos/PUC/MLA-machine-learning-avancado/hulk.jpeg')
    imagem = open(path, 'rb').read()
