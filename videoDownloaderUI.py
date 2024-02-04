import customtkinter as ctk
import videodownloader as vd
import os

# set theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# create root window
root = ctk.CTk()
root.geometry("500x350")
root.minsize(500, 350)
root.title("Youtube Downloader")

videoDownloadFrame = ctk.CTkFrame(master=root)
videoDownloadFrame.pack(pady= 20, padx = 60,fill="both", expand=True)

label = ctk.CTkLabel(master=videoDownloadFrame, text="Digite o link do video", font=("Arial", 20))
label.pack(pady=12, padx = 10)

videoLink = ctk.CTkEntry(master=videoDownloadFrame, font=("Arial", 14))
videoLink.pack(pady=12, padx = 10)

def downloading():
    videoDownloadFrame.pack_forget()
    
    videoDownloadingScreen = ctk.CTkFrame(master=root)
    videoDownloadingScreen.pack(pady= 20, padx = 60,fill="both", expand=True)
    
    downloadFolder = os.path.join(os.path.expanduser("~"), "Downloads")

    if vd.validateVideoLink(videoLink.get()) == True:
        downloadingLabel = ctk.CTkLabel(master=videoDownloadingScreen, text="Baixando video...", font=("Arial", 20))
        downloadingLabel.pack(pady=12, padx = 10)

        dowloadingProgressBar = ctk.CTkProgressBar(master=videoDownloadingScreen, )
        dowloadingProgressBar.pack(pady=12, padx = 10)

        vd.videoDownload(videoLink.get(), downloadFolder)
        
        label = ctk.CTkLabel(master=videoDownloadingScreen, text="Video Baixado", font=("Arial", 20))
        label.pack(pady=12, padx = 10)

        def tryAgain():
            videoDownloadingScreen.pack_forget()
            videoDownloadFrame.pack(pady= 20, padx = 60,fill="both", expand=True)
            videoLink.delete(0, "end")

        tryagainButton = ctk.CTkButton(master=videoDownloadingScreen, text="Baixar outro video", command= tryAgain)
        tryagainButton.pack(pady=12, padx = 10)

    else:
        label = ctk.CTkLabel(master=videoDownloadingScreen, text="Video indisponivel!", font=("Arial", 20))
        label.pack(pady=12, padx = 10)

        def tryAgain():
            videoDownloadingScreen.pack_forget()
            videoDownloadFrame.pack(pady= 20, padx = 60,fill="both", expand=True)
            videoLink.delete(0, "end")

        tryagainButton = ctk.CTkButton(master=videoDownloadFrame, text="Tentar novamente", command= tryAgain)
        tryagainButton.pack(pady=12, padx = 10)
    

videoButton = ctk.CTkButton(master=videoDownloadFrame, text="Baixar", command= downloading)
videoButton.pack(pady=12, padx = 10)

backButton = ctk.CTkButton(master=videoDownloadFrame, text="Sair", command= root.destroy)
backButton.pack(pady=12, padx = 10)

root.mainloop()