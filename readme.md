# Classificação de cães e gatos

## Uso:

:point_right: Instalar as dependências:
```sh
pip install -r requirements.txt
```

:point_right: Iniciar o servidor:
```sh
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

:point_right: Teste:
```python
import requests as r

path_imagem = 'caminho/da/sua/imagem'

imagem = open(path_imagem, 'rb').read()

response = r.post('http://localhost:8000', files={'imagem': imagem})

print(response.json()['classifica'])
```
