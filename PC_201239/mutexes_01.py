import threading
from pytube import YouTube


mutex = threading.Lock()

def descarga(vid):
    yt = YouTube(vid)
    video=  yt.streams.filter(file_extension='mp4').order_by('resolution').first()
    video.download(destino)
    print("el video descargado en: "+destino)

class Hilo(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        video=id
        self.id=video


    def run(self):
        mutex.acquire()
        descarga(self.id)
        mutex.release()

destino="C:/Users/Yurandier/OneDrive/Escritorio/python/videos"

Hilos = [Hilo('https://www.youtube.com/watch?v=hoQmSA6MRAk'), Hilo('https://www.youtube.com/watch?v=jgXIT9ewqhk'), Hilo('https://www.youtube.com/watch?v=GO5utuvcZps'), Hilo('https://www.youtube.com/watch?v=NLyD2K8yLS0'),
Hilo('https://www.youtube.com/watch?v=nwrqQ2jYpwY'), Hilo('https://www.youtube.com/watch?v=6GCNUeTFSbA'), Hilo('https://www.youtube.com/watch?v=HzdD8kbDzZA'), Hilo('https://www.youtube.com/watch?v=xkmgcvr5Ezc'), Hilo('https://www.youtube.com/watch?v=mK7CI3XHYjs'),
Hilo('https://www.youtube.com/watch?v=2sMGX_52_hs')]

for h in Hilos:
    h.start()