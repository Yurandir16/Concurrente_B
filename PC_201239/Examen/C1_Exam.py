import argparse
import threading
import time
import random

estadoFilosofo = None
candados = []
CANTIDAD_FILOSOFOS = 0 
RAFAGA_COMER = 0
TOTAL_TIEMPO_COMER = 0   

ESTADO_ESPERANDO = "F"
ESTADO_COMIENDO = "C"

def startSimulacion(id_fil):

    intentos_fallidos = 0
    tiempo_comiendo = 0

    while tiempo_comiendo < TOTAL_TIEMPO_COMER:
        if agarrarPalillos(id_fil):

            intentos_fallidos = 0

            tiempo_comer = min(RAFAGA_COMER, TOTAL_TIEMPO_COMER - tiempo_comiendo)
            tiempo_comiendo += tiempo_comer
            print(f"[+] Filosofo: {id_fil} comiendo [{tiempo_comer} seg.]")
            time.sleep(tiempo_comiendo)
            dejarPalillos(id_fil)

            estadoFilosofo[id_fil] = ESTADO_ESPERANDO
            tiempo_espera = random.uniform(0, 5)
            print(f"[*] Filosofo: {id_fil} esperando[{tiempo_espera:.2f} seg.]")
            time.sleep(tiempo_espera)
        else:
            estadoFilosofo[id_fil] = ESTADO_ESPERANDO
            intentos_fallidos += 1

            
            tiempo_reintentar = random.uniform(0, 3)
            print(f"[ ] Filosofo: {id_fil} esperando palillos"
                f" Intento {intentos_fallidos} [{tiempo_reintentar:.2f} seg.]")
            time.sleep(tiempo_reintentar)

def agarrarPalillos(id_filosofo):

    palillo_izq = candados[id_filosofo]
    palillo_der = candados[(id_filosofo - 1) % CANTIDAD_FILOSOFOS]

    palillo_izq.acquire()

    if palillo_der.acquire(blocking=False):
        return True
    else:
        palillo_izq.release()
        return False


def dejarPalillos(id_filosofo):

    candados[id_filosofo].release()
    candados[(id_filosofo - 1) % CANTIDAD_FILOSOFOS].release()
        
def obtenerDatos():

    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--num_filosofos", 
                        type=int, default=8)
    parser.add_argument("-r", "--rafaga_comer", 
                        type=int, default=4)
    parser.add_argument("-t", "--tiempo_total", 
                        type=int, default=10)
    return parser.parse_args()

if __name__ == '__main__':
    args = obtenerDatos()

    CANTIDAD_FILOSOFOS = args.num_filosofos
    RAFAGA_COMER = args.rafaga_comer
    TOTAL_TIEMPO_COMER = args.tiempo_total

    estadoFilosofo = CANTIDAD_FILOSOFOS * [ESTADO_ESPERANDO]

    for _ in range(CANTIDAD_FILOSOFOS):
        candados.append(threading.RLock())

    hilos = []
    for i in range(args.num_filosofos):
        nuevo_hilo = threading.Thread(target=startSimulacion, args=(i,))
        hilos.append(nuevo_hilo)
    
    for hilo in hilos:
        hilo.start()

    for hilo in hilos:
        hilo.join()