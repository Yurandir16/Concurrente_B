import time
from pytube import YouTube

def download_video():
    urls_video = ["https://www.youtube.com/watch?v=3GQvsthnjeE",
    "https://www.youtube.com/watch?v=tIpzfs5tBJU",
    "https://www.youtube.com/watch?v=qcR1KbbhRTs",
    "https://www.youtube.com/watch?v=lYdXgHbnQX4",
    "https://www.youtube.com/watch?v=VuDc8HQ3Rbg"]
    
    destino = ("C:/Users/Yurandier/OneDrive/Escritorio/python/videos")
    for link in urls_video:
      yt = YouTube(link)
      video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first() 
      save_video(video,destino)


def save_video(video,destino):    
    video.download(destino)
    print("Se ha descargado los videos"+destino)


if __name__ == "__main__":
    init_time = time.time()
    download_video()
    end_time = time.time()-init_time
    print(end_time)
