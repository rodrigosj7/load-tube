from recept_links import recept_links
from treating_link import capture_link
from mp4_to_mp3 import convert_mp4_for_mp3
from mp4_to_wav import convert_mp4_for_wav
from download_media import download_media

PATH_VIDEOS = './downloads/videos'
PATH_MUSICS = './downloads/musics'

def download_format_mp4():
	all_links = recept_links()
	download_media(capture_link(all_links),PATH_VIDEOS)

def download_format_mp3():
	all_links = recept_links()
	title = download_media(capture_link(all_links),PATH_MUSICS)
	convert_mp4_for_mp3(PATH_MUSICS, title)

def download_format_wav():
	all_links = recept_links()
	title = download_media(capture_link(all_links),PATH_MUSICS)
	convert_mp4_for_wav(PATH_MUSICS, title)
