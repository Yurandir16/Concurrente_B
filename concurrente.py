import time
from unittest import result
import json
import requests
import mysql.connector
import threading
import concurrent.futures

threading_local = threading.local()

def service(url_site):
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(get_service,url_site)

def get_service(url_site):
    data = requests.get(url_site)
    if data.status_code == 200:
        data = data.json()
        results = data.get('results', [])
        if results:
            for x in results:
                pokename = x['name']
                write_db(pokename)


def write_db(pokename):
 conexion = mysql.connector.connect(
        user='root',
        password='200116qw',
        host='localhost',
        database='Pokemones',
        port='3306'
    )
 mycursor = conexion.cursor()
 sql = "INSERT INTO poke(pokename) VALUES ('{0}')".format(pokename)
 mycursor.execute(sql)
 conexion.commit()

if __name__ == "__main__":
    url_site = {'https://pokeapi.co/api/v2/pokemon?limit=1154&offset=0'}
    init_time = time.time() 
    service(url_site)
    end_time = time.time()-init_time
    print(end_time)


