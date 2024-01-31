import customtkinter as ctk
import videodownloader as vd

# set theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# create root window
root = ctk.CTk()
root.geometry("500x350")
root.minsize(500, 350)
root.title("Youtube Downloader")

frame = ctk.CTkFrame(master=root)
frame.pack(pady= 20, padx = 60,fill="both", expand=True)

# videoDownloadScreen = ctk.CTkBaseClass(master=frame)
# mainMenuScreen = ctk.CTkBaseClass(master=frame)

# def videoDownloadPage():
#     videoDownloadScreen.pack(fill="both", expand=True)

#     label = ctk.CTkLabel(master=videoDownloadScreen, text="Digite o link do video", font=("Arial", 20))
#     label.pack(pady=12, padx = 10)

#     # videoLink = ctk.CTkEntry(master=videoDownloadScreen, font=("Arial", 14))
#     # videoLink.pack(pady=12, padx = 10)
    
#     # def downloading():
#     #     vd.videoDownload(videoLink.get())
#     #     progressBar = ctk.CTkProgressBar(master=videoDownloadScreen, value=0, maximum=100)
#     #     progressBar.pack(pady=12, padx = 10)
#     #     progressBar.start()


#     # videoButton = ctk.CTkButton(master=videoDownloadScreen, text="Baixar", command=downloading)
#     # videoButton.pack(pady=12, padx = 10)
    
#     # backButton = ctk.CTkButton(master=videoDownloadScreen, text="Voltar", command=videoDownloadScreen.destroy)
#     # backButton.pack(pady=12, padx = 10)

# def mainMenu():
#     mainMenuScreen.pack(fill="both", expand=True)

#     label = ctk.CTkLabel(master=mainMenuScreen, text="O QUE QUER BAIXAR?", font=("Arial", 20))
#     label.pack(pady=12, padx = 10)

#     videoButton = ctk.CTkButton(master=mainMenuScreen, text="Video Único", command=videoDownloadPage)
#     videoButton.pack(pady=12, padx = 10)


root.mainloop()