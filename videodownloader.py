from pytube import YouTube, Playlist
from pathlib import Path
from tqdm import *
from pywebio.input import *
from pywebio.output import *

pathToDownload = (r"C:\Users\silga\Downloads")

# videoLink = input(label= "Link do video") 
videoLink = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

def on_progress(stream, chunk, bytes_remaining):
    pbar.update(len(chunk))

videoYoutubeObject = YouTube(videoLink)

stream = videoYoutubeObject.streams.get_highest_resolution()
pbar = tqdm(desc= stream.title,total=stream.filesize, unit="B", unit_scale=True, colour="red")

videoYoutubeObject.register_on_progress_callback(on_progress)

stream.download(pathToDownload)