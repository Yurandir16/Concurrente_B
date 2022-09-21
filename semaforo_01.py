from threading import Thread, Semaphore
from turtle import st
from urllib import request
from pytube import YouTube
semaforo = Semaphore(1)


def download_video():
    urls_video = 'https://www.youtube.com/watch?v=3GQvsthnjeE'
    destino = ("C:/Users/Yurandier/OneDrive/Escritorio/python/videos")
    
    yt = YouTube(urls_video)
    video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first() 
    save_video(video,destino)

def save_video(video,destino):    
    video.download(destino)
    print("El video se ha descargado:"+destino)

def download_music():
    url_music="https://www.youtube.com/watch?v=Ij65wvAGX-c&list=RDGMEMYH9CUrFO7CfLJpaD7UR85w&start_radio=1&rv=a5uQMwRMHcs"
    destino2=("C:/Users/Yurandier/OneDrive/Escritorio/python/music")

    yt = YouTube(url_music)
    music= yt.streams.filter(only_audio=True).first()
    save_music(destino2,music)

def save_music(destino2,music):
    music.download(destino2)
    print("La cancion a sido descagada:"+destino2)


def download_imagen():
    urls_imagen = 'https://www.playstation.com/en-us/games/dark-souls-iii/'
    destino = ("C:/Users/Yurandier/OneDrive/Escritorio/python/images")
    
    local_name_imagen='dark.jpg'
    imagen= request.get(urls_imagen).content
    with open(local_name_imagen, 'wb')as handler:
        handler.write(imagen)
    save_imagen(imagen)

def save_imagen(imagen):    
    print("Se ha descargado la imagen:")
    

class Hilo(Thread):
    def __init__(self, id):
        Thread.__init__(self)
        self.id=id

    def run(self):
        semaforo.acquire()
        crito(self.id)
        semaforo.release()



