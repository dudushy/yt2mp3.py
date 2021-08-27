# imports
import youtube_dl, os

# functions
def clear():
    os.system('cls') #'cls' for Win // 'clear' for Linux

# main
yturl = input("Please insert YouTube URL: ")
video = youtube_dl.YoutubeDL().extract_info(
    url = yturl,download=False
    )
options={
    'format':'bestaudio/best',
    'keepvideo':False,
    'outtmpl': f"{video['title']}.mp3"
    }

with youtube_dl.YoutubeDL(options) as ydl:
    ydl.download([video['webpage_url']])

print(f"Download complete... {video['title']}.mp3")