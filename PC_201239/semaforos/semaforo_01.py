from threading import Thread, Semaphore
from pytube import YouTube
semaforo = Semaphore(1)


def descarga(vid):
    yt = YouTube(vid)
    video=  yt.streams.filter(file_extension='mp4').order_by('resolution').first()
    video.download(destino)
    print("el video se ha descargado en: "+destino)

class Hilo(Thread):
    def __init__(self, id):
        Thread.__init__(self)
        video=id
        self.id=video

    def run(self):
        semaforo.acquire()
        descarga(self.id)
        semaforo.release()

destino=r"C:/Users/Yurandier/OneDrive/Escritorio/python/videos"
threads_semaphore = [Hilo('https://www.youtube.com/watch?v=hoQmSA6MRAk'), Hilo('https://www.youtube.com/watch?v=jgXIT9ewqhk'), Hilo('https://www.youtube.com/watch?v=GO5utuvcZps'), Hilo('https://www.youtube.com/watch?v=NLyD2K8yLS0'),
Hilo('https://www.youtube.com/watch?v=nwrqQ2jYpwY'), Hilo('https://www.youtube.com/watch?v=6GCNUeTFSbA'), Hilo('https://www.youtube.com/watch?v=HzdD8kbDzZA'), Hilo('https://www.youtube.com/watch?v=xkmgcvr5Ezc'), Hilo('https://www.youtube.com/watch?v=mK7CI3XHYjs'),
Hilo('https://www.youtube.com/watch?v=2sMGX_52_hs')]

for t in threads_semaphore:
    t.start()