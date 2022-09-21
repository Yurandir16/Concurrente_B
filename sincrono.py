import time
from unittest import result
import json
import requests

# Investigar sobre la libreria threading en python


def get_service():
    urlPoke = 'https://pokeapi.co/api/v2/pokemon?limit=10&offset=0'
    data = requests.get(urlPoke)
    if data.status_code == 200:
        data = data.json()
        results = data.get('results', [])
        if results:
            for x in results:
                name = x['name']
                print(name)
    # Implementar requests
    # consumir un servicio que descarge por lo menos 5000 registros
    # utilizar un for
    # for x in data:
     # write_db(x.name)


def write_db():


if __name__ == "__main__":
    get_service()
