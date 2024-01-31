from pytube import YouTube, Playlist
from tqdm import *

pathToDownload = (r"C:\Users\silga\Downloads\_Videos baixados")

def videoDownload(videoLink):

    if videoLink.startswith("https://www.youtube.com/watch?v=") or videoLink.startswith("https://youtu.be/"):
        videoYoutubeObject = YouTube(videoLink)
        stream = videoYoutubeObject.streams.get_highest_resolution()

        # def on_progress(stream, chunk, bytes_remaining):
        #     pbar.update(len(chunk))

        # pbar = tqdm(desc= stream.title,total=stream.filesize, unit="B", unit_scale=True, colour="red")

        # videoYoutubeObject.register_on_progress_callback(on_progress)

        def onProgress():
            return videoYoutubeObject.register_on_progress_callback()

        stream.download(pathToDownload)
    else:
        print("Video indisponivel!")
        return

def audioDownload():
    videoLink = input("Digite o link do video: \n")

    videoYoutubeObject = YouTube(videoLink)

    stream = videoYoutubeObject.streams.get_audio_only()

    def on_progress(stream, chunk, bytes_remaining):
        pbar.update(len(chunk))

    pbar = tqdm(desc= stream.title,total=stream.filesize, unit="B", unit_scale=True, colour="red")

    videoYoutubeObject.register_on_progress_callback(on_progress)

    stream.download(pathToDownload)


def playlistVideoDownload():
    playlistLink = input("Digite o link da playlist: \n")

    playlistObject = Playlist(playlistLink)

    for video in playlistObject.video_urls:
        videoUrl = YouTube(video)
        stream = videoUrl.streams.get_highest_resolution()
        pbar = tqdm(total=stream.filesize, unit="B", unit_scale=True, colour="red")

        def on_progress(stream, chunk, bytes_remaining):
            pbar.update(len(chunk))

        videoUrl.register_on_progress_callback(on_progress)
        stream.download(pathToDownload)
        pbar.close()
        print("Download successfully completed!")


def selectVideoOrPlaylist():
    return input("O QUE QUER BAIXAR?\n"
          "p = playlist\n"
          "v = video unico\n")
    

def selectAudioOrVideo():
    return input("O QUE QUER BAIXAR?\n"
          "v = video completo\n"
          "a = apenas audio\n")
