from join_all import *
from interaction import interaction

options = [1,2,3]

response = interaction(options)

if response == 1:
    download_format_mp4()

if response == 2:
    download_format_mp3()

if response == 3:
    download_format_wav()
    