import threading
import time
import concurrent.futures
import requests

def service():
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(verificar())

def verificar():
 url_site = ["https://www.facebook.com/",
    "https://www.apple.com",
    "https://www.google.com",
    "https://www.aliexpress.com",
    "https://www.figma.com/",
    "https://www.walmart.com.mx/",
    "https://www.amazon.com.mx/",
    "https://trello.com/", 
    "https://www.youtube.com/",
    "https://www.netflix.com/mx/",
    "https://www.disneyplus.com/es-mx",
    "https://open.spotify.com/",
    "https://cinepolis.com/",
    "https://www.nike.com/mx/",
    "https://www.suburbia.com.mx/tienda/home",
    "https://web.telegram.org/",
    "https://discord.com/",
    "https://www.disneyplus.com",
    "https://code.visualstudio.com/",
    "https://web.whatsapp.com/",
    "https://www.mercadolibre.com.mx",
    "https://twitter.com/",
    "https://www.shoppe.com.mx",
    "https://www.hbomax.com",
    "https://www.paramountplus.com"]

 for link in url_site:
    data = requests.head(link)
    if data.status_code == 200:
        print(data.status_code, '<-Sitio activo:'+link)
    else:
        print(data.status_code, '<-sitio no activo:'+link)


if __name__ == "__main__":

    while True:
        init_time = time.time()
        th1 = threading.Thread(target=service)
        th1.start()
        th1.join()
        end_time = time.time()-init_time
        print("Tiempo de ejecucion =>", end_time)
        time.sleep(240)