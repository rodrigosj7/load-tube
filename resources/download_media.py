from pytube import YouTube

def download_media(links,path):
    for link in links:
        print('Baixando...' + link)
        yt = YouTube(link)
        ys = yt.streams.filter(only_audio=True).first()
        ys.download(path)
        title = yt.title
        
    return title