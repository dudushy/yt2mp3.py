# imports
from pytube import YouTube
import os

# functions
def clear():
    os.system('cls') #'cls' for Win // 'clear' for Linux

# main
clear()
try:
    yt = YouTube(input('Please insert YouTube URL: ')) #yt url

    output = yt.streams.filter(only_audio=True).first().download(output_path='\MP3s')
    print(f'\n{output}')
except Exception as e:
    print(f'\n{e}')
