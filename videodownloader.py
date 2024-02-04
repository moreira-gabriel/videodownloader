from pytube import YouTube
from tqdm import *

def validateVideoLink(videoLink):
    if videoLink.startswith("https://www.youtube.com/watch?v=") or videoLink.startswith("https://youtu.be/"):
        return True
    else:
        return False

def videoDownload(videoLink, pathToDownload):
    if validateVideoLink(videoLink) == True:
        videoYoutubeObject = YouTube(videoLink)
        stream = videoYoutubeObject.streams.get_highest_resolution()

        # def on_progress(stream, chunk, bytes_remaining):
        #     pbar.update(len(chunk))

        # pbar = tqdm(desc= stream.title,total=stream.filesize, unit="B", unit_scale=True, colour="red")

        # def onProgress():
        #     print(videoYoutubeObject.register_on_progress_callback())
        #     return videoYoutubeObject.register_on_progress_callback()
        
        # videoYoutubeObject.register_on_progress_callback(on_progress)

        stream.download(pathToDownload)
        # pbar.close()
        print("Download successfully completed!")
    else:
        print("Invalid video link!")
